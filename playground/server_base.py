from threading import Lock, RLock, Thread, Condition
from rx import Observable as O
from rx.core import Scheduler
import select
import time
import logging
import sys
logging.basicConfig(level=logging.DEBUG,
                    stream=sys.stdout,
                    format='%(asctime)s %(levelname)s %(process)d %(threadName)s %(message)s' )

logger = logging.getLogger(__name__)

o = RLock()
condition = Condition(o)

def complete():
#    condition.release()
    logger.info('Fin')

observer = {
    'on_next': logger.info,
    'on_completed': complete
}

if __name__ == '__main__':
    sub = O.interval(1000)\
        .observe_on(Scheduler.event_loop)\
        .take(5)\
        .subscribe(**observer)

    O.never().subscribe(**observer)
    logger.info('exiting')