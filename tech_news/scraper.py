import requests
import time
import math
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        http = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if http.status_code != 200:
        return None
    return http.text


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    comments_count = selector.css("#js-comments-btn::text").re_first(r"\d+")
    writer = selector.css(".tec--author__info__link::text").get()
    data = {
        "url": selector.css("meta[property='og:url']::attr(content)").get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": writer.strip() if writer else writer,
        "shares_count": (int(shares_count) if shares_count else 0),
        "comments_count": (int(comments_count) if comments_count else 0),
        "summary": "".join(
            selector.css(
                ".tec--article__body > p:first-child *::text"
            ).getall()
        ),
        "sources": list(
            map(
                str.strip,
                selector.css("div.z--mb-16 .tec--badge::text").getall(),
            )
        ),
        "categories": list(
            map(
                str.strip,
                selector.css("div#js-categories a.tec--badge::text").getall(),
            )
        ),
    }
    return data


# print(scrape_noticia(fetch("https://www.tecmundo.com.br/novidades")))


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css("h3 > a.tec--card__title__link::attr(href)").getall()


# print(scrape_novidades(fetch("https://www.tecmundo.com.br/novidades")))


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css("a.tec--btn::attr(href)").get()


print(scrape_next_page_link(fetch("https://www.tecmundo.com.br/novidades")))


# Requisito 5
def get_tech_news(amount):
    noticias = []
    url_list = []
    url = "https://www.tecmundo.com.br/novidades"
    for _ in range(math.ceil(amount / 20)):
        data = fetch(url)
        url_novidades = scrape_novidades(data)
        for url_item in url_novidades:
            url_list.append(url_item)
            url = scrape_next_page_link(data)
    for index in range(amount):
        noticias.append(scrape_noticia(fetch(url_list[index])))
    create_news(noticias)
    return noticias
