import requests
import time
import tech_news.scraper_services as scraper

# Requisito 1


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        return response.text if response.status_code == 200 else None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    return scraper.get_attributes_of(html_content)


# Requisito 3 class="tec--list__item"
def scrape_novidades(html_content):
    url_list = scraper.get_many(
        html_content,
        'main a[class="tec--card__title__link"]::attr(href)',
    )
    return url_list


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
