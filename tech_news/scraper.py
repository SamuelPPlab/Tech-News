import requests
import time
from parsel import Selector
from helpers.status_code import SUCCESS
from tech_news.database import create_news


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == SUCCESS:
            return response.text
        return None
    except requests.Timeout:
        return None


def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr( datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get()
    if writer:
        writer = writer.strip()
    else:
        writer = None
    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count:
        shares_count = int(shares_count.split()[0])
    else:
        shares_count = 0
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments_count:
        comments_count = int(comments_count)
    else:
        comments_count = 0
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
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


def scrape_novidades(html_content):
    selector = Selector(html_content)
    url = selector.css("h3 > a.tec--card__title__link::attr(href)").getall()
    return url


def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css("div.tec--list > a:last-child::attr(href)").get()


def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    content_html = fetch(url)
    news_links = scrape_novidades(content_html)
    news_saved = 0
    news_for_save = []
    while amount > len(news_links):
        url = scrape_next_page_link(content_html)
        content_html = fetch(url)
        news_links = news_links + scrape_novidades(content_html)
    while news_saved < amount:
        next_content = fetch(news_links[news_saved])
        next_news = scrape_noticia(next_content)
        news_for_save.append(next_news)
        news_saved += 1
    create_news(news_for_save)
    return news_for_save
