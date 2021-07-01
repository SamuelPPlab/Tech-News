import requests
import time


# Requisito 1
def fetch(url):
    time.sleep(1)
    response = requests.get(url)
    if(response.status_code == 200):
        print(response.text)
        return response.content["Content-Type"]
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
