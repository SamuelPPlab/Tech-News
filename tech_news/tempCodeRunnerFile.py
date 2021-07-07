import requests
import time
from parsel import Selector
import re

url = "https://www.tecmundo.com.br/novidades"
response = requests.get(url, timeout=3)
print(response.text)
selector = Selector(response)
url = selector.css("a.tec--card__title__link").get()