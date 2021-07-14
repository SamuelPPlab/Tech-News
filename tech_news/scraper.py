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
    selector = Selector(html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get().strip()
    shares = selector.css(".tec--toolbar__item::text").get().split()[0]
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
        "writer": writer,
        "shares_count": int(shares) if shares else 0,
        "comments_count": int(comments_count),
        "summary": "".join(summary),
        "sources": [source.strip() for source in sources],
        "categories": [category.strip() for category in categories],
    }


# Requisito 3
def scrape_novidades(html_content):
    return Selector(html_content).css(
        ".tec--card__info h3 a::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    return Selector(html_content).css(
        ".tec--list > a::attr(href)"
    ).get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
