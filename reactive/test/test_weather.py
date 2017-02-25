import pytest
import logging
from reactive.weather import *
import time


logger = logging.getLogger(__name__)


def test_hot_observable():
    location = (43.15132, -77.620632)
    s = hot_observable(location).subscribe(logger.info)
    time.sleep(30)
