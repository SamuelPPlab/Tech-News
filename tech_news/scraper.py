import requests
import time
from parsel import Selector

# import database

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

    writer = selector.css(".tec--author__info__link::text").get()
    if writer:
        writer = writer.strip()

    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count:
        shares_count = int(shares_count.split("Compartilharam")[0])

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments_count:
        comments_count = int(comments_count)

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
    list_news = []
    selector = Selector(text=html_content)
    for item in selector.css(
        ".tec--list--lg .tec--card__title__link::attr(href)"
    ).getall():
        list_news.append(item)
    return list_news


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_button = selector.css(".tec--btn--primary::attr(href)").get()
    return next_button


# Requisito 5
def get_tech_news(amount):
    resp_fetch = fetch("https://www.tecmundo.com.br/novidades")
    list_news = scrape_novidades(resp_fetch)
    for item in list_news:
        resp_fecth_new = fetch(item)
        content_new = scrape_noticia(resp_fecth_new)
        print(content_new)
    # data = database.get_collection()
    # return data
