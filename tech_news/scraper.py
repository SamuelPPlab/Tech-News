import time
import requests
from math import ceil
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)

        if (response.status_code == 200):
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    new = {}
    selector = Selector(text=html_content)
    new['url'] = selector.css("meta[property='og:url']::attr(content)").get()
    new['title'] = selector.css(".tec--article__header__title::text").get()
    new['timestamp'] = selector.css("time::attr(datetime)").get()
    new['writer'] = selector.css(
        ".tec--author__info__link::text"
    ).get()
    if new['writer'] is not None:
        new['writer'] = new['writer'].strip()

    new['shares_count'] = selector.css(
        ".tec--toolbar__item::text"
    ).get()

    if new['shares_count']:
        new['shares_count'] = int(new['shares_count'].split(' ')[1])
    else:
        new['shares_count'] = 0

    new['comments_count'] = selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get()

    if new['comments_count']:
        new['comments_count'] = int(new['comments_count'])
    else:
        new['comments_count'] = 0

    new['summary'] = "".join(selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall())
    new['sources'] = list(map(str.strip, selector.css(
        ".z--mb-16 div a.tec--badge::text"
    ).getall()))
    new['categories'] = list(map(str.strip, selector.css(
        "div#js-categories a.tec--badge::text"
    ).getall()))

    return new


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(
      "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(
      "div.tec--list a.tec--btn::attr(href)"
    ).get()


# Requisito 5
def get_tech_news(amount):
    scraped_news = []
    page = fetch("https://www.tecmundo.com.br/novidades")
    links_news = scrape_novidades(page)

    total_pages = ceil(amount / 20)
    print(total_pages)

    if total_pages > 1:
        for _ in range(1, total_pages):
            page = scrape_next_page_link(page)
            next_page_content = fetch(page)
            next_page_news = scrape_novidades(next_page_content)
            links_news = links_news + next_page_news

    for link in links_news:
        news = fetch(link)
        scraped_news.append(scrape_noticia(news))
        if len(scraped_news) == amount:
            break
    create_news(scraped_news)
    return scraped_news
