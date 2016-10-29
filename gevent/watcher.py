import select
from rx import Observable, Observer
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

logger = logging.getLogger(__name__)


def file_source(file):
    return open(file, 'r')


def watch(handle):
    return select.select([handle], [], [], 5)


def print_f(value):
    print value


def handle_select(value):
    if ([], [], []) == value:
        logger.info('Nothing happening...')
    else:
        return value[0][0].readline()


Observable.just(sys.stdin) \
    .map(watch) \
    .map(handle_select) \
    .filter(bool) \
    .repeat() \
    .subscribe(on_next=logger.info)
