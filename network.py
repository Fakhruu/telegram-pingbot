import requests


def is_web_up(url):
    r = requests.head(url)
    return r.status_code == 200


