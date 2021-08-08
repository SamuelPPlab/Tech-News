import requests
import time


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        return None
    finally:
        if (response.status_code == 200):
            return response.headers["Content-Type"]
        else:
            return None


def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


def get_tech_news(amount):
    """Seu código deve vir aqui"""
