# Requisito 1
import requests
from time import sleep
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout
from tech_news.database import create_news


def fetch(url):
    """Seu código deve vir aqui"""
    try:
        sleep(1)
        response = requests.get(url, timeout=3)
        return None if response.status_code != 200 else response.text
    except ReadTimeout:
        return None


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
