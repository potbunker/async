from lessons import *
from rx import Observable as O


source0 = O.from_(range(10))
source1 = O.just('value is')
obs = {
    'on_next': lambda x: logger.info(x),
    'on_error': lambda e: logger.error(e.message, e),
    'on_completed': lambda: logger.info('Completed')
}


def example1():
    dis = source0.subscribe(**obs)
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
