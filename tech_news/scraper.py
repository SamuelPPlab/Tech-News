import requests
import time


LINK = "https://www.tecmundo.com.br/novidades"


# Requisito 1
def fetch(url):
    try:
        resquest_url = requests.get(url, timeout=3)
        time.sleep(1)
        print(resquest_url.status_code)
        status = resquest_url.status_code
        if status != 200:
            return None
        html = resquest_url.text
        return html
    except requests.Timeout:
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
