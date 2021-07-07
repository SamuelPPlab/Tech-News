import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if response.status_code != 200:
        return None
    return response.text


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    share_count = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    comments_count = selector.css("#js-comments-btn::text").re_first(r"\d+")
    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    sources = selector.css("div.z--mb-16 .tec--badge::text").getall()
    categories = selector.css("div#js-categories a.tec--badge::text").getall()
    newsInfo = {
        "url": selector.css("meta[property='og:url']::attr(content)").get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": selector.css(".tec--author__info__link::text").get().strip(),
        "shares_count": int(share_count),
        "comments_count": int(comments_count),
        "summary": "".join(summary),
        "sources": list(map(str.strip, sources)),
        "categories": list(map(str.strip, categories))
    }
    return newsInfo


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css("h3 > .tec--card__title__link::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    nextPageUrl = selector.css(".tec--btn::attr(href)").get()
    return nextPageUrl


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
