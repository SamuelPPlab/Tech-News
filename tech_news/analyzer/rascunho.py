import requests
import time
from parsel import Selector
import re

url = "https://www.tecmundo.com.br/novidades"
response = requests.get(url, timeout=3)
selector = Selector(response.text)
list = selector.css("h3 > a::attr(href)").getall()
print(list)
