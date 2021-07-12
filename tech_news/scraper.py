# from pymongo import database
import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        return response.text
    except (requests.ReadTimeout, requests.HTTPError):
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("head link[rel='canonical']::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    writer = selector.css(".tec--author__info__link::text").get()
    writer = writer.strip()
    shares_count = selector.css(".tec--toolbar__item::text").get()
    shares = int(shares_count[1:2])
    comments_count = int(selector.css(".tec--btn::attr(data-count)").get())
    sum = selector.css(".tec--article__body p:first-child *::text").getall()
    summary = "".join(sum)
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    for i in range(len(sources)):
        sources[i] = sources[i].strip()
    categories = selector.css(".tec--badge--primary::text").getall()
    for i in range(len(categories)):
        categories[i] = categories[i].strip()
    print(writer)
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    noticias = selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()
    return noticias


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    nextPage = selector.css(
        ".tec--btn::attr(href)"
    ).get()
    return nextPage


# Requisito 5
def get_tech_news(amount):
    print(amount)
