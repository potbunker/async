from reactive import logger
from psycopg2.pool import SimpleConnectionPool
from rx import Observable as O
from rx.core import Scheduler
from time import time
from select import select


dsn = {
    'host': 'localhost',
    'port': 5432,
    'user': 'event_store_dev',
    'password': 'gdtmr0ll',
    'database': 'event_store'
}


pool = SimpleConnectionPool(minconn=1, maxconn=5, **dsn)


def generate(channel, n):
    conn = pool.getconn()
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute('select pg_notify(%s, %s)', (channel, '%.10f' % time()))
    pool.putconn(conn)


def listen(channel):
    conn = pool.getconn()
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute('LISTEN {}'.format(channel))

    def to_events(conn):
        conn.poll()
        while conn.notifies:
            yield conn.notifies.pop(0)

    return O.just(conn)\
        .map(lambda c: select([c], [], [], 5))\
        .repeat()\
        .filter(lambda x: x[0])\
        .map(lambda x: x[0][0])\
        .switch_map(lambda c: O.from_(to_events(conn)))


if __name__ == '__main__':

    def payload(notify):
        return notify.payload

    def diff(emit_time):
        return time() - float(emit_time)

    def acc(left, n):
        left['sum'] = left['sum'] + n
        left['count'] = left['count'] + 1
        return left

    d0 = O.interval(100).map(lambda n: generate('event', n)).subscribe(lambda n: n)

    o = O.defer(lambda: listen('event')).take(100)

    d1 = o\
        .map(payload).map(diff)\
        .reduce(acc, {'sum': 0.0, 'count': 0})\
        .map(lambda n: n['sum']/n['count'])\
        .subscribe(logger.info)
    d2 = o\
        .map(payload).map(diff)\
        .reduce(acc, {'sum': 0.0, 'count': 0})\
        .map(lambda n: n['sum']/n['count'])\
        .subscribe(logger.info)


    input('a')
