import time
import requests
from requests.exceptions import HTTPError, ReadTimeout


def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except (ReadTimeout or HTTPError):
        return None
    finally:
        return response.headers["Content-Type"]


def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


def get_tech_news(amount):
    """Seu código deve vir aqui"""
