from rx import Observable as O
from rx.core import Scheduler
from reactive import logger
import sys

def output():
    def out(x):
#        logger.info(x)
        return O.timer(1000).map(lambda n: x)
    source = O.from_('Hello world!').switch_map(out)
    return source

out = sys.stdout

s = output()\
    .subscribe(lambda x: out.write(x), None, lambda: out.write('\n'))


import time
time.sleep(10)