import requests
import time
from parsel import Selector
# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        res = requests.get(url, timeout=3)
        res.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(error)
        return None
    else:
        return res.text




# Requisito 2
def scrape_noticia(html_content):
    


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
