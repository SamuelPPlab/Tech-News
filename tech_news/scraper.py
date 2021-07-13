import requests
import time

def url_ok(request):
    return request.status_code == 200

# Requisito 1
# Baseado em: https://github.com/tryber/sd-07-tech-news/blob/nonato-tech-news/tech_news/scraper.py
def fetch(url):
    try:
        time.sleep(1)
        page = requests.get(url)
        if url_ok(page):
            return page.text
        return None

    except requests.ReadTimeout:
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
