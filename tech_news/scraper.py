import requests
import time
import math
from parsel import Selector
from tech_news.database import create_news

# import pprint


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=1)
        response.raise_for_status()
    except Exception:
        return None
    else:
        return response.text


def stripper(word):
    return word.strip()


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return {
        "url": selector.css("head > [rel=canonical]::attr(href)").get(),
        "title": selector.css("h1.tec--article__header__title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": selector.css("a.tec--author__info__link::text").get().strip()
        if selector.css(".tec--author__info__link::text")
        else None,
        "shares_count": int(
            selector.css("div.tec--toolbar__item::text").get().split()[0]
        )
        if selector.css("div.tec--toolbar__item::text")
        else 0,
        "comments_count": int(
            selector.css("button.tec--btn::attr(data-count)").get()
        )
        if selector.css("button.tec--btn::attr(data-count)")
        else 0,
        "summary": "".join(
            selector.css(
                ".tec--article__body > p:first-child *::text"
            ).getall()
        ),
        "sources": list(
            map(
                stripper,
                selector.css("div.z--mb-16 a.tec--badge::text").getall(),
            )
        ),
        "categories": list(
            map(stripper, selector.css("a.tec--badge--primary::text").getall())
        ),
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(".tec--list__item h3 > a::attr(href)").getall() or []


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css("div.tec--list > a::attr(href)").get() or None


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    pages = math.ceil(amount / 20)
    url = "https://www.tecmundo.com.br/novidades"
    pageCount = 0
    newsCollection = []
    while pageCount < pages:
        html_content = fetch(url)
        list = scrape_novidades(html_content)
        for one_News in list:
            if len(newsCollection) < amount:
                newsCollection.append(scrape_noticia(fetch(one_News)))
        pageCount += 1
        url = scrape_next_page_link(html_content)
    create_news(newsCollection)
    return newsCollection


# print(get_tech_news(20))
