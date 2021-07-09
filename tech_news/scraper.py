import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code != 200:
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    new = {}
    selector = Selector(html_content)
    new["url"] = selector.css("head > link[rel='canonical']::attr(href)").get()
    new["title"] = selector.css(".tec--article__header__title::text").get()
    new["timestamp"] = selector.css("#js-article-date::attr(datetime)").get()
    new["writer"] = selector.css(
        ".tec--author__info__link::text").get().strip()
    new["shares_count"] = int(
        selector.css(".tec--toolbar__item::text").get().strip(" Compartilh")
    )
    new["comments_count"] = int(selector.css(
        "#js-comments-btn::attr(data-count)").get()
    )
    summary = selector.css(
        ".tec--article__body p:first-child *::text").getall()
    new["summary"] = "".join(summary)
    sources = selector.css(
        "a[class='tec--badge']::text").getall()
    new["sources"] = [source.strip() for source in sources]
    categories = selector.css(
        "#js-categories a::text").getall()
    new["categories"] = [category.strip() for category in categories]
    return new


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
