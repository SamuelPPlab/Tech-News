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


# Requisito 2
def scrape_noticia(html_content):

    selector = Selector(text=html_content)

    scraped_url = selector.css("head link[rel=canonical]::attr(href)").get()

    scraped_title = selector.css("h1.tec--article__header__title::text").get()

    scraped_timestamp = selector.css(
        "div.tec--timestamp__item time::attr(datetime)"
    ).get()

    scraped_writer = selector.css("a.tec--author__info__link::text").get()

    scraped_source = selector.css(".z--mb-16 .tec--badge::text").getall()

    scraped_categories = selector.css("div#js-categories a::text").getall()

    if scraped_writer:
        scraped_writer = scraped_writer.strip()
    scraped_shares_count = selector.css("div.tec--toolbar__item::text").get()

    if scraped_shares_count:
        scraped_shares_count = int(
            (scraped_shares_count.strip()).split(" ")[0]
        )
    else:
        scraped_shares_count = 0
    scraped_comments_count = selector.css("div.tec--toolbar__item::text").get()

    if scraped_comments_count:
        scraped_comments_count = int(
            (scraped_comments_count.strip()).split(" ")[0]
        )
    else:
        scraped_comments_count = 0
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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
