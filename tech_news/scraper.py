import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        sleep(2)
        url_search = (
            url if url is not None else "https://www.tecmundo.com.br/novidades"
        )
        response = requests.get(url_search, timeout=3)
        return response.text if response.status_code == 200 else None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    # noticia_info = {}
    selector = Selector(html_content)
    print(selector)


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
