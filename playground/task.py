from rx import Observable as O
from rx.core import Scheduler
import logging
logger = logging.getLogger(__name__)


def run(count):
    return O.timer(0, 2000).take(count).switch_map(lambda n: O.from_(range(n)))\
        .do_action(logger.info)