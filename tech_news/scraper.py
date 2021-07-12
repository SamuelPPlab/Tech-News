import time
import requests
from requests.exceptions import HTTPError, ReadTimeout
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except ReadTimeout:
        return None

    try:
        response.raise_for_status()
    except HTTPError:
        return None

    return response.text


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    author = selector.css(".tec--author__info__link::text").get().strip()
    shares = selector.css(".tec--toolbar__item::text").get().split()[0]
    shares_count = int(shares) if shares else 0
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    summary = selector.css(
        ".tec--article__body p:nth-child(1) *::text"
    ).getall()
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories .tec--badge::text").getall()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": author,
        "shares_count": shares_count,
        "comments_count": int(comments_count),
        "summary": "".join(summary),
        "sources": [source.strip() for source in sources],
        "categories": [category.strip() for category in categories],
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links = selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()
    return links


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next = selector.css(".tec--btn::attr(href)").get()
    return next


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
