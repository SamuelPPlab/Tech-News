import requests
import time

from parsel import Selector


# Requisito 1
def fetch(url):

    try:
        response = requests.get(url, timeout=3)
        print(1)
    except requests.ReadTimeout:
        print(2)
        return None
    # response = requests.get(url)
    selector = Selector(text=response.text)
    # time.sleep(1)

    if response.status_code != 200:
        print(3)
        return None

    print(4)
    return print(selector.data)


fetch("https://app.betrybe.com/")