import requests
import time

# import math

from parsel import Selector

# from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)  # Rate Limit de 1

    try:
        response = requests.get(url, timeout=3)
        print(response)

        if response.status_code != 200:
            return None
        return response.text

    except requests.Timeout:  # acima de 3 segundos Timeout
        return None


# Vitor Rodrigues


def get_scraped_shares_count(selector):
    selected_text = selector.css(".tec--toolbar__item::text").get()
    for i in selected_text.split():
        if i.isdigit():
            return int(i)


def get_scraped_comments_count(selector):
    selected_text = selector.css(".tec--btn::text").get()
    for i in selected_text.split():
        if i.isdigit():
            return int(i)


# Requisito 2
def scrape_noticia(html_content):

    selector = Selector(html_content)

    scraped_shares_count = 0

    scraped_comments_count = 0

    scraped_url = selector.css("head link[rel=canonical]::attr(href)").get()

    scraped_title = selector.css(".tec--article__header__title::text").get()

    scraped_timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()

    scraped_writer = (
        selector.css(".tec--author__info__link::text").get().strip()
        if len(selector.css(".tec--author__info__link")) >= 1
        else None
    )

    scraped_source = selector.css(".z--mb-16 div a.tec--badge::text").getall()

    scraped_categories = selector.css(".tec--badge--primary::text").getall()

    scraped_shares = selector.css(".tec--toolbar__item")

    scraped_comments = selector.css(".tec--btn")

    if len(scraped_shares) != 0:
        scraped_shares_count = (
            get_scraped_shares_count(selector)
            if get_scraped_shares_count(selector) is not None
            else 0
        )

    if len(scraped_comments) != 0:
        scraped_comments_count = (
            get_scraped_comments_count(selector)
            if get_scraped_comments_count(selector) is not None
            else 0
        )

    scraped_summary = selector.css(
        ".tec--article__body p:first-child *::text"
    ).getall()

    return {
        "url": scraped_url,
        "title": scraped_title,
        "timestamp": scraped_timestamp,
        "writer": scraped_writer,
        "shares_count": scraped_shares_count,
        "comments_count": scraped_comments_count,
        "summary": "".join(scraped_summary),
        "sources": [source.strip() for source in scraped_source],
        "categories": [category.strip() for category in scraped_categories],
    }


# Vanessa Bidinoto


# Requisito 3
def scrape_novidades(html_content):

    selector = Selector(html_content)

    scraped_urls = selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()

    return scraped_urls if len(scraped_urls) >= 1 else []


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
