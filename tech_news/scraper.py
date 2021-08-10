import requests
import time
from parsel import Selector
from tech_news.database import create_news


def fetch(url):
    try:
        result = requests.get(url, timeout=5)
        time.sleep(1)
    except requests.ReadTimeout:
        return None

    if (result.ok):
        return result.text


def scrape_noticia(html_content):
    sel = Selector(html_content)

    categoriesRaw = sel.css("#js-categories > a::text").getall()
    categories = [category.strip() for category in categoriesRaw]

    author = sel.css(".tec--author__info__link::text").get()
    if author:
        author = author.strip()
    else:
        author = None

    shareCount = sel.css(".tec--toolbar__item::text").get()
    if shareCount is None:
        shareCount = 0
    else:
        shareCount = str(
            sel.css(".tec--toolbar__item::text").get()
        ).split()[0]

    commentCount = sel.css("#js-comments-btn::attr(data-count)").get()
    if commentCount is None:
        commentCount = 0

    summary = sel.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()

    return {
        "url": sel.css("head link[rel=canonical]::attr(href)").get(),
        "title": sel.css("#js-article-title::text").get(),
        "timestamp": sel.css("#js-article-date::attr(datetime)").get(),
        "writer": author,
        "shares_count": int(shareCount),
        "comments_count": int(commentCount),
        "summary": "".join(summary),
        "sources": [
            source.strip()
            for source in sel.css(".z--mb-16 div a::text").getall()
        ],
        "categories": categories,
    }


def scrape_novidades(html_content):
    se = Selector(html_content)
    try:
        return se.css(".tec--list__item article div h3 a::attr(href)").getall()
    except Exception:
        return list()


def scrape_next_page_link(html_content):
    sel = Selector(html_content)
    try:
        return sel.css(".tec--btn::attr(href)").get()
    except Exception:
        return None


def get_tech_news(amount):
    news = list()
    page_url = "https://www.tecmundo.com.br/novidades"

    while len(news) < amount:
        fResult = fetch(page_url)
        urls = scrape_novidades(fResult)
        for url in urls:
            nPage = scrape_noticia(fetch(url))
            if len(news) < amount:
                news.append(nPage)
        page_url = scrape_next_page_link(fResult)

    create_news(news)
    return news
