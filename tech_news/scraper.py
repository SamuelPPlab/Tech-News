import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            response = None
            return response
        return response.text
    except requests.ReadTimeout:
        response = None
        return response


# Requisito 2
def scrape_noticia(html_content):
    result = {}
    selector = Selector(text=html_content)
    result["url"] = selector.css("link[rel=canonical]::attr(href)").get()
    result["title"] = selector.css("h1#js-article-title::text").get().strip()
    result["timestamp"] = selector.css(
        "time#js-article-date::attr(datetime)"
    ).get()
    if selector.css("a.tec--author__info__link::text"):
        result["writer"] = selector.css(
            "a.tec--author__info__link::text"
        ).get().strip()
    else:
        result["writer"] = None
    if selector.css("div.tec--toolbar__item::text"):
        result["shares_count"] = int(selector.css(
            "div.tec--toolbar__item::text"
        ).get().strip()[0])
    else:
        result["shares_count"] = 0
    if selector.css("button#js-comments-btn::text"):
        result["comments_count"] = int(selector.css(
            "button#js-comments-btn::attr(data-count)"
        ).get())
    else:
        result["comments_count"] = 0
    result["summary"] = "".join(selector.css(
        "div.tec--article__body p:first-child *::text"
        ).getall())
    result["sources"] = []
    for source in selector.css("div.z--mb-16 a.tec--badge::text").getall():
        result["sources"].append(source.strip())
    result["categories"] = []
    for category in selector.css("div#js-categories a::text").getall():
        result["categories"].append(category.strip())
    return result


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    list = []
    if selector.css("h3 a.tec--card__title__link"):
        list = selector.css("h3 a.tec--card__title__link::attr(href)").getall()
    else:
        list = []
    return list


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    result = None
    if selector.css("a.z--mx-auto"):
        result = selector.css("a.z--mx-auto::attr(href)").get()
        return result
    else:
        return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
