import requests
import time
from parsel import Selector

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
    sources = []
    categories = []
    selector = Selector(text=html_content)

    title = selector.css(".tec--article__header__title::text").get()

    url = selector.css("head > link[rel=canonical]::attr(href)").get()

    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()

    writer = selector.css(".tec--author__info__link::text").get().strip()

    shares_count = int(
        selector.css(".tec--toolbar__item::text")
        .get()
        .split("Compartilharam")[0]
    )

    comments_count = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )

    summary = "".join(
        selector.css(".tec--article__body p:first-child *::text").getall()
    )

    for item in selector.css(".z--mb-16 .tec--badge::text").getall():
        sources.append(item.strip())

    for item in selector.css(".tec--badge--primary::text").getall():
        categories.append(item.strip())

    return {
        "title": title,
        "url": url,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    noticias_listadas = []
    selector = Selector(text=html_content)
    for item in selector.css(
        ".tec--list--lg .tec--card__title__link::attr(href)"
    ).getall():
        noticias_listadas.append(item)
    return noticias_listadas


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
