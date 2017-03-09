from lessons import *
from rx import Observable as O


source0 = O.interval(2000).map(lambda x: 'source0 {}'.format(x)).take(5)
source1 = O.just('value is')
source2 = O.interval(150).map(lambda x: 'source2 {}'.format(x)).take(30)


obs = {
    'on_next': logger.info,
    'on_error': lambda e: logger.error(e),
    'on_completed': lambda: logger.info('Completed')
}


def example1():
    dis = source0\
        .merge(source2)\
        .subscribe(**obs)
    dis.dispose()


def example2():
    dis = source0\
        .concat(source2)\
        .subscribe(**obs)
    dis.dispose()


def example3():
    dis = source0\
        .switch_map(lambda x: source2.map(lambda y: '{} - {}'.format(x, y)))\
        .subscribe(**obs)
    dis.dispose()


def example4():
    def acc(a, b):
        a.append(b)
        return a
    dis = source0\
        .do_action(logger.info)\
        .reduce(acc, [])\
        .subscribe(**obs)
    dis.dispose()


def example5():
    def acc(a, b):
        a.append(b)
        return a
    dis = source0\
        .do_action(logger.info)\
        .scan(acc, [])\
        .subscribe(**obs)
    dis.dispose()


def example6():
    dis = O.zip(source0, source1.repeat(), source2, lambda a, b, c: (a, b, c))\
        .subscribe(**obs)
    dis.dispose()


if __name__ == '__main__':
    example1()
    example2()
    example3()
    example4()
    example5()
    example6()
