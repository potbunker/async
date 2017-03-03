from threading import Lock, RLock, Thread, Condition
from rx import Observable as O
from rx.core import Scheduler
from Queue import Queue
import signal
import logging
import sys
logging.basicConfig(level=logging.DEBUG,
                    stream=sys.stdout,
                    format='%(asctime)s %(levelname)s %(process)d %(threadName)s %(message)s' )

logger = logging.getLogger(__name__)


def complete():
    signal.setitimer(signal.ITIMER_REAL, 0.001, 1)
    logger.info('Fin')

observer = {
    'on_next': logger.info,
    'on_completed': complete
}


def handler(signum, frame):
    import traceback
    logger.info('signal {} received. {}'.format(signum, frame))
    traceback.print_stack(frame)

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, handler)
    signal.signal(signal.SIGTERM, handler)

    sub = O.timer(0, 1000, Scheduler.timeout)\
        .take(20)\
        .subscribe(**observer)

    signal.pause()

    logger.info('exiting')