import time

import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        response.status_code

        if response.status_code == 200:
            return response.text
        else:
            return None

    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    list = selector.css("h3 a.tec--card__title__link::attr(href)").getall()
    return list


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next = selector.css(".tec--btn::attr(href)").get()
    return next


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
