
import time
import requests
from parsel import Selector


# Requisito 1

def fetch(url):
    try:
        response = requests.get(url)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if response.status_code != 200:
        return None
    return response.text


# Requisito 2

def scrape_noticia(html_content):   
    """Seu código deve vir aqui"""
    all_news = {}
    selector = Selector(text=html_content)

    all_news['url'] = selector.css("link[ rel=canonical] ::attr(href)").get()

    all_news['title'] = selector.css("#js-article-title::text").get()

    all_news['timestamp'] = selector.css(
        "#js-article-date ::attr(datetime)").get()

    all_news['writer'] = (selector.css(
        ".tec--author__info__link::text").get().strip()
        if selector.css(".tec--author__info__link::text").get() else None)

    all_news["shares_count"] = int(
        selector.css(".tec--toolbar__item::text")
        .get(default="0")
        .replace("Compartilharam", "")
        .strip()
    )

    all_news['comments_count'] = int(selector.css(
        "#js-comments-btn ::attr(data-count)").get())

    all_news['summary'] = "".join(selector.css(
        ".tec--article__body > p:first-child *::text").getall())
    all_news['sources'] = list(map(str.strip, selector.css(
        ".z--mb-16 .tec--badge::text").getall()))

    all_news['categories'] = list(map(str.strip, selector.css(
        "#js-categories a ::text").getall()))

    return all_news


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css("h3 > .tec--card__title__link::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(".tec--btn::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
