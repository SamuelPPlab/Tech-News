import requests
import time
from tech_news.database import create_news
from requests.exceptions import ReadTimeout
from parsel import Selector

# Requisito 1
def fetch(url):
    
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
    except ReadTimeout:
        return None