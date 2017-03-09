import signal
import logging
import sys
import os
import threading
logging.basicConfig(level=logging.INFO,
                    stream=sys.stdout,
                    format='%(asctime)s %(levelname)s %(process)d %(threadName)s %(message)s' )

logger = logging.getLogger(__name__)


def run_daemon(target, args=(), kwargs={}):
    observer = {
        'on_next': logger.debug,
        'on_completed': lambda: logger.info('Complete')
    }

    def handler(signum, frame):
        import traceback
        logger.info('signal {} received. {}'.format(signum, frame))
        traceback.print_stack(frame)

    signals = [
        signal.SIGINT,
        signal.SIGTERM,
        signal.SIGQUIT
    ]

    map(lambda sig: signal.signal(sig, handler), signals)
    sub = target(*args, **kwargs)\
        .finally_action(lambda: os.kill(os.getpid(), signal.SIGTERM))\
        .subscribe(**observer)
    signal.pause()
    from threading import enumerate
    for t in enumerate():
        if not t.daemon and t.is_alive():
            logger.info(t)
    sub.dispose()

    logger.info('exiting: {}'.format(''))

if __name__ == '__main__':
    from task import run
    run_daemon(run, (5,))
