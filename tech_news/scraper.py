import requests
import time
from parsel import Selector

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None

    time.sleep(1)

    if response.ok:
        return response.text
    else:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    categories_aux = selector.css("#js-categories > a::text").getall()
    categories = [category.strip() for category in categories_aux]

    writer = selector.css(".tec--author__info__link::text").get()
    # referência: Carol Andradre
    if writer:
        writer = writer.strip()
    else:
        writer = None

    counts = selector.css("#js-author-bar nav div::text").get()
    if counts is None:
        counts = 0
    else:
        counts = str(
            selector.css("#js-author-bar nav div::text").get()
        ).split()[0]

    comments = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments is None:
        comments = 0

    get_summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()  # referência: Carol Andrade

    return {
        "url": selector.css("head > link:nth-child(26)")
        .css("link::attr(href)")
        .get(),
        "title": selector.css("h1::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": writer,
        "shares_count": int(counts),
        "comments_count": int(comments),
        "summary": "".join(get_summary),
        "sources": [
            source.strip()
            for source in selector.css(".z--mb-16 div a::text").getall()
        ],
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(
        ".tec--list__item article div h3 a::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(".tec--btn::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    html_news = []
    page = "https://www.tecmundo.com.br/novidades"
    while len(html_news) < amount:
        html = fetch(page)
        urls = scrape_novidades(html)
        for url in urls:
            new = scrape_noticia(fetch(url))
            html_news.append(new)
            if len(html_news) == amount:
                create_news(html_news)
                return html_news
        page = scrape_next_page_link(html)
# requisito 5
