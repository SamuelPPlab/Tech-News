import requests
import time
# import math

# from parsel import Selector
# from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)  # Rate Limit de 1

    try:
        response = requests.get(url, timeout=3)
        print(response)

        if response.status_code != 200:
            return None
        return response.text

    except requests.Timeout:  # acima de 3 segundos Timeout
        return None
# Vitor Rodrigues


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
