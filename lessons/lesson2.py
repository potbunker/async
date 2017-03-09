from lessons import *
from rx import Observable as O
from rx.core import Scheduler


source0 = O.interval(1000).take(5).observe_on(Scheduler.event_loop)
source1 = O.from_([
    'first',
    'second',
    'third',
    'fourth'
]).repeat(2)


obs = {
    'on_next': logger.info,
    'on_error': lambda e: logger.error(e.message, e),
    'on_completed': lambda: logger.info('Completed')
}


def example1():
    dis = source1\
        .merge(source0)\
        .switch_map(lambda x: O.just(x))\
        .subscribe_on(Scheduler.event_loop)\
        .subscribe(**obs)
    dis.dispose()


def example2():
    dis = source0\
        .filter(lambda x: x % 2 == 0)\
        .subscribe(**obs)
    dis.dispose()


def example3():
    dis = source0\
        .filter(lambda x: x % 2 == 0)\
        .map(lambda x: 'value is {}'.format(x))\
        .subscribe(**obs)
    dis.dispose()


def example4():
    dis = source0\
        .filter(lambda x: x % 2 == 0)\
        .reduce(lambda a, b: a + b, 0)\
        .subscribe(**obs)
    dis.dispose()


def example5():
    dis = source0\
        .filter(lambda x: x % 2 == 0)\
        .scan(lambda a, b: a + b, 0)\
        .subscribe(**obs)
    dis.dispose()


def example6():
    dis = O.zip(source0, source1.repeat(), lambda a, b: '{} {}'.format(b, a))\
        .subscribe(**obs)
    dis.dispose()


if __name__ == '__main__':
    example1()
    example2()
    example3()
    example4()
    example5()
    example6()
