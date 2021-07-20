import requests
import time
import math
from tech_news.database import create_news
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if response.status_code == 200:
        return response.text


# Requisito 2
def scrape_noticia(html_context):
    selector = Selector(html_context)
    url = selector.css("meta[property='og:url'] ::attr(content)").get()
    url_title = selector.css(".tec--article__header__title ::text").get()
    url_timestamp = selector.css("time#js-article-date ::attr(datetime)").get()
    url_writer = selector.css(".tec--author__info__link ::text").get()
    url_shares_count = "".join(
        char
        for char in selector.css("div.tec--toolbar__item ::text").get()
        if char.isdigit()
    )
    url_comments_count = int(
        selector.css(
            "button#js-comments-btn.tec--btn ::attr(data-count)"
        ).get()
    )
    url_summary = selector.css(
        ".tec--article__body > p:first-child ::text"
    ).getall()
    url_source = selector.css(".z--mb-16 a::text").getall()
    url_categories = selector.css("#js-categories a::text").getall()
    url_dicio = {
        "url": url,
        "title": url_title,
        "timestamp": url_timestamp,
        "writer": url_writer.strip() if url_writer else None,
        "shares_count": int(url_shares_count if url_shares_count else 0),
        "comments_count": int(url_comments_count if url_comments_count else 0),
        "summary": "".join(url_summary),
        "sources": list(map(str.strip, url_source)),
        "categories": list(map(str.strip, url_categories)),
    }
    return url_dicio


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    urls = selector.css("h3 > a.tec--card__title__link ::attr(href)").getall()
    return urls


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css(
        "a.tec--btn.tec--btn--lg.tec--btn--primary.z--mx"
        "-auto.z--mt-48 ::attr(href)"
    ).get()
    return next_page


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    url_list = []
    data_list = []
    if amount <= 20:
        page = scrape_novidades(fetch(url))
        for index in page:
            url_list.append(index)
    pages_number = math.ceil(amount / 20)
    for index in range(pages_number):
        page = scrape_novidades(fetch(url))
        url = scrape_next_page_link(fetch(url))
        for index in page:
            url_list.append(index)
    for index in range(amount):
        data_list.append(scrape_noticia(fetch(url_list[index])))
    print(len(url_list))
    create_news(data_list)
    return data_list
