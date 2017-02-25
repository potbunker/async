import json
import logging

from reactive.weather import get_weather

logger = logging.getLogger(__name__)


def test_get_weather():
    longitude=43.151325
    latitude=-77.620632
    weather = get_weather((longitude, latitude))
    weather.repeat(10)\
        .map(lambda x: json.loads(x.text)) \
        .subscribe(logger.info)

