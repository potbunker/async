import pytest
from gevent.weather import get_weather
import logging
import json


logger = logging.getLogger(__name__)


def test_get_weather():
    longitude=43.151325
    latitude=-77.620632
    weather = get_weather((longitude, latitude))
    logger.info(json.loads(weather.text))

