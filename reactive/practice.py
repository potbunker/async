from rx import Observable as O
from rx.core import Scheduler
from reactive import *
from random import randint
import time

def supplier(obs):

    value = randint(0, 1000)
    if not value:
        obs.on_complete()
    elif value % 13:
        obs.on_error(RuntimeError)
    else:
        obs.on_next(value)

def backoff_functions():
    return O.generate(2, lambda n: True, lambda n: n*2, lambda n: n if n < 120 else 120).start_with(0)

def run():
    logger.info('running')
    o0 = O.interval(200).switch_map(lambda n: O.create(supplier)).retry(2).take(2)
    s0 = o0.subscribe(logger.info)

    o1 = backoff_functions().take(5).do_action(logger.warn)
    s1 = o1.subscribe(logger.info)

#    s1 = backoff_functions().subscribe(logger.info)
    input('waiting ...')
    s0.dispose()


if __name__ == '__main__':
    run()
