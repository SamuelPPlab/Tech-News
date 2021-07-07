import requests
import time
from parsel import Selector
import re

# Requisito 1


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2


def scrape_noticia(html_content):

    categories = []
    sources = []

    selector = Selector(html_content)
    url = selector.css("head > meta[property='og:url']::attr(content)").get()
    title = selector.css("#js-article-title::text").get()
    writer = (
        selector.css(
            "#js-author-bar > div > \
            p.z--m-none.z--truncate.z--font-bold > a::text"
        )
        .get()
        .strip()
    )
    shares_count = (
        (selector.css("#js-author-bar > nav > div::text").get())
        .replace(" ", "")
        .replace("Compartilharam", "")
    )
    comments_count = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )
    summary = selector.css(
        "#js-main > div.z--container > article > div.tec--article__body-grid \
        > div.tec--article__body.z--px-16.p402_premium > p:nth-child(1)"
    ).get()
    summary = re.sub(
        "<[^>]+?>", "", summary
    )
    # https://pt.stackoverflow.com/questions/192176/como-remover-tags-em-um-texto-em-python
    sourcesdiv = selector.css(
        "#js-main > div.z--container > article > \
        div.tec--article__body-grid > div.z--mb-16.z--px-16 > div > a::text"
    ).getall()
    categoriesdiv = selector.css("#js-categories a::text").getall()

    for categorie in categoriesdiv:
        categories.append(categorie.strip())

    for source in sourcesdiv:
        sources.append(source.strip())

    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    newsList = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }

    return newsList


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    list = selector.css("h3 > a::attr(href)").getall()
    return list


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
