import requests
import time
import parsel
from requests.exceptions import HTTPError, ReadTimeout


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if(response.status_code == 200):
            return response.text
    except ReadTimeout:
        return None

    except HTTPError:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)

    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date ::attr(datetime)").get()

    is_writer = selector.css(".tec--author__info__link::text").get()
    if (is_writer):
        writer = is_writer.strip()
    else:
        writer = None

    is_shares_count = selector.css("tec--toolbar__item::text").get()
    if (is_shares_count):
        shares_count = int(is_shares_count.split()[0])
    else:
        shares_count = 0

    is_comments_count = selector.css(
        "#js-comments-btn::attr(data-count)").get()
    if (is_comments_count):
        comments_count = int(is_comments_count.split()[0])
    else:
        comments_count = 0

    # referência: Tiago Esdras
    summary = "".join(selector.css(
        ".tec--article__body > p:first-child *::text").getall())

    # referência: Tiago Esdras
    sources = list(map(str.strip, selector.css(
        ".z--mb-16 .tec--badge::text").getall()))

    # referência: Tiago Esdras
    categories = list(map(str.strip, selector.css(
        "#js-categories a ::text").getall()))

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    urls = selector.css("h3 a::attr(href)").getall()

    return urls


# Requisito 4
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    url = selector.css("a.tec--btn::attr(href)").get()
    return url or None


# Requisito 5
def get_tech_news(amount):
    """faça seu códido aqui"""
