from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    data = {}
    data["url"] = selector.css(
        "head link[rel=canonical]::attr(href)"
    ).get()
    data["title"] = selector.css(
        ".tec--article__header__title::text"
    ).get()
    data["timestamp"] = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    data["writer"] = (
        selector.css(".tec--author__info__link::text").get().strip()
    )
    data["shares_count"] = (
        selector.css(".tec--toolbar__item svg").get()
    )
    print(data)


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links = selector.css(
        ".tec--card__title a::attr(href)"
    ).getall()
    print(links)
    return links


scrape_novidades(fetch(
    "https://www.tecmundo.com.br/novidades"
))


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
