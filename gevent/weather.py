import requests
from rx import Observable
from rx.core import Scheduler


KEY = 'e53ff04d1f77e92adad9a4ec86a353f2'
URI = 'https://api.darksky.net/forecast/{}'.format(KEY)


def get_weather(location):
    with requests.session() as session:
        endpoint = '{}/{},{}'.format(URI, location[0], location[1])
        return Observable.just(session, scheduler=Scheduler.current_thread) \
            .map(lambda x: x.get(endpoint)) \
            .interval(1000)
