import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code != 200:
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    new = {}
    selector = Selector(html_content)
    new["url"] = selector.css("head > link[rel='canonical']::attr(href)").get()
    new["title"] = selector.css(".tec--article__header__title::text").get()
    new["timestamp"] = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(
        ".tec--author__info__link::text").get()
    if writer is not None:
        new["writer"] = writer.strip()
    else:
        new["writer"] = None
    shares = selector.css(".tec--toolbar__item::text").get()
    if shares is not None:
        new["shares_count"] = int(shares.strip(" Compartilh"))
    else:
        new["shares_count"] = 0
    comments = selector.css(
        "#js-comments-btn::attr(data-count)").get()
    if comments is not None:
        new["comments_count"] = int(comments)
    else:
        new["comments_count"] = 0
    summary = selector.css(
        ".tec--article__body > p:first-child *::text").getall()
    new["summary"] = "".join(summary)
    sources = selector.css(
        "a[class='tec--badge']::text").getall()
    new["sources"] = [source.strip() for source in sources]
    categories = selector.css(
        "#js-categories a::text").getall()
    new["categories"] = [category.strip() for category in categories]
    return new


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    urls = selector.css(
        ".tec--card__info h3 a::attr(href)").getall()
    return urls


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css(
        ".tec--list > a::attr(href)").get()
    return next_page_link


# Requisito 5
def get_tech_news(amount):
    base_url = "https://www.tecmundo.com.br/novidades"
    news = []

    while len(news) < amount:
        response = fetch(base_url)
        news_links = scrape_novidades(response)
        base_url = scrape_next_page_link(response)

        for new in news_links:
            content = fetch(new)
            new_content = scrape_noticia(content)
            if len(news) < amount:
                news.append(new_content)
            else:
                break

    create_news(news)
    return news
