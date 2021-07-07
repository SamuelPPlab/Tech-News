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


# Chave summary foi montada consultando o pr do vitor-rc1
# https://github.com/tryber/sd-07-tech-news/pull/1/files
# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    comments_count = selector.css("#js-comments-btn::text").re_first(r"\d+")
    dictionary = {
        "url": selector.css("meta[property='og:url']::attr(content)").get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": selector.css(".tec--author__info__link::text").get().strip(),
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "categories": list(map(
            str.strip, selector.css("div#js-categories a.tec--badge::text")
            .getall())),
        "sources": list(map(
            str.strip, selector.css("div.z--mb-16 .tec--badge::text")
            .getall())),
        "summary": "".join(selector.css(
         ".tec--article__body > p:first-child *::text"
        ).getall())
    }
    return dictionary


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    url = selector.css("h3 > a.tec--card__title__link::attr(href)").getall()
    return url


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
