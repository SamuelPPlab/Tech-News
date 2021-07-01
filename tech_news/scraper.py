import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    result = {}
    selector = Selector(text=html_content)
    result["url"] = selector.css(
        "meta[property='og:url']::attr(content)"
    ).get()
    result["title"] = selector.css("#js-article-title::text").get()
    result["timestamp"] = selector.css(
        "#js-article-date::attr(datetime)"
    ).get()
    result["writer"] = (
        selector.css(".tec--author__info__link::text").get()[1:-1] or None
    )
    result["shares_count"] = (
        int(selector.css(".tec--toolbar__item::text").get()[1]) or 0
    )
    result["comments_count"] = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )
    result["summary"] = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    result["sources"] = list(map(str.strip, sources))
    categories = selector.css("#js-categories .tec--badge::text").getall()
    result["categories"] = list(map(str.strip, categories))

    return result


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(".tec--list__item h3 > a::attr(href)").getall() or []


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
