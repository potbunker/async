from rx import Observable, Observer

from reactive.weather import get_weather


def start():
    longitude=43.151325
    latitude=-77.620632
    a = Observer()

    source = Observable.interval(10000)
    source.subscribe(
        lambda n: a.onNext( get_weather((longitude, latitude)))
    )

start()

print 'Done'