import requests

KEY='e53ff04d1f77e92adad9a4ec86a353f2'
URI='https://api.darksky.net/forecast/{}'.format(KEY)


def get_weather(location):
    with requests.session() as session:
        endpoint='{}/{},{}'.format(URI, location[0], location[1])
        response = session.get(endpoint)
        return response



