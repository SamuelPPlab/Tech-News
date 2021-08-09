import requests
import time
from parsel import Selector
from math import ceil
from tech_news.database import create_news

# Requisito 1


def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    time.sleep(1)
    if response.status_code != 200:
        return None
    return response.text


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    shares = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    summary = selector.css(
        "div.tec--article__body > p:nth-child(1) *::text"
    ).getall()
    sourcesStrip = selector.css(".z--mb-16 .tec--badge::text").getall()
    writer = selector.css(".tec--author__info__link::text").get()
    sources = []
    categories = []
    for source in sourcesStrip:
        sources.append(source.strip())
    categoriesStrip = selector.css("#js-categories > a *::text").getall()
    for categorie in categoriesStrip:
        categories.append(categorie.strip())
    comments = selector.css("#js-comments-btn ::attr(data-count)").get()

    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".tec--article__header__title ::text").get(),
        "timestamp": selector.css(
            ".tec--timestamp__item time ::attr(datetime)"
        ).get(),
        "writer": writer.strip() if writer else writer,
        "shares_count": int(shares) if shares else 0,
        "comments_count": int(comments) if comments else 0,
        "summary": "".join(summary),
        "sources": sources,
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    allUrls = selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()
    return allUrls if allUrls else []


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    nextUrl = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 >"
        "div.tec--list.tec--list--lg > a::attr(href)"
    ).get()
    return nextUrl if nextUrl else None


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    nextPageAmount = amount / 20
    url = "https://www.tecmundo.com.br/novidades"
    allUrls = []
    for _ in range(ceil(nextPageAmount)):
        pageHTML = fetch(url)
        allUrls.extend(scrape_novidades(pageHTML))
        url = scrape_next_page_link(pageHTML)
    allUrls = allUrls[:amount]

    allNewsDict = []
    for item in allUrls:
        news = fetch(item)
        allNewsDict.append(scrape_noticia(news))
    create_news(allNewsDict)
    return allNewsDict
