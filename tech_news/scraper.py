import requests
import time

SUCCESS = 200

# Requisito 1


def fetch(url):
    try:
        response = requests.get(url, timeout=2)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if response.status_code == SUCCESS:
        return response.text
    else:
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
