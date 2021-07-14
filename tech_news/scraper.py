import requests
import time
from parsel import Selector
from helpers.status_code import OK

# Requisito 1


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == OK:
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("meta[property='og:url']::attr(content)").get()
    timestamp = selector.css("#js-article-date::attr( datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get()
    shares_count = selector.css(
        "#js-author-bar > nav > div:nth-child(1)::text"
    ).get()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    return {
        "url": url,
        "title": selector.css("#js-article-title::text").get(),
        "timestamp": timestamp,
        "writer": writer.strip() if writer is not None else None,
        "shares_count": int(shares_count.split()[0]),
        "comments_count": int(comments_count),
        "summary": "".join(selector.css(
            ".tec--article__body > p:first-child *::text"
        ).getall()),
        "sources": list(map(
            str.strip,
            selector.css("div.z--mb-16 .tec--badge::text").getall(),
        )),
        "categories": [
            categoria.strip()
            for categoria in selector.css(
                "div#js-categories a.tec--badge::text"
            ).getall()
        ],
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    url = selector.css("h3 > a.tec--card__title__link::attr(href)").getall()
    return url


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css("div.tec--list > a:last-child::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
