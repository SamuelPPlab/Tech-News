import requests
from time import sleep


# Requisito 1
def fetch(url):
    try:
        resposta = requests.get(url, timeout=3)
        sleep(1)
        if (resposta.status_code != 200):
            raise Exception('Deu ruim')
        return resposta.text
    except:
        return None


# Requisito 2
def scrape_noticia(html_content):
    ""


# Requisito 3
def scrape_novidades(html_content):
    ""


# Requisito 4
def scrape_next_page_link(html_content):
    ""


# Requisito 5
def get_tech_news(amount):
    ""
