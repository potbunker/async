from rx import Observable as O
from rx.core import Scheduler
from reactive import *
from random import randint
import signal


rand = O.from_(randint(0, 10) for n in range(100))


def supplier(obs):
    value = randint(0, 10)
    obs.on_next(value) if value else obs.on_completed()


def backoff_functions():
    return O.generate(2, lambda n: True, lambda n: n*2, lambda n: n if n < 120 else 120).start_with(0)


def run():
    logger.info('running')
    o0 = O.interval(100).map(lambda n: (n, randint(0, 10))).take(100)\
        .group_by(key_selector=lambda n: n[1], element_selector=lambda n: n)
#        .map(lambda n: O.zip(O.repeat(n.key), n, lambda a, b: (a, b)))
    s0 = o0.subscribe(lambda n: n.subscribe(lambda x: logger.info('%d - %s' % (n.key, x))))

    signal.pause()
    s0.dispose()


if __name__ == '__main__':
    rand.subscribe(logger.info)
    run()
