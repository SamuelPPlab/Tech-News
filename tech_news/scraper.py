import time
import requests
import math
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        res_tec_mundo = requests.get(url)
        time.sleep(1)
        if res_tec_mundo.status_code == 200:
            return res_tec_mundo.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    new_dict = {
        "url": selector.css("meta[property='og:url']::attr(content)").get(),
        "title": selector.css("#js-article-title::text").get(),
        "timestamp": selector.css("time::attr(datetime)").get(),
        "writer": selector.css(".tec--author__info__link::text").get().strip(),
        "shares_count": int(
            selector.css(".tec--toolbar__item::text").re_first(r"\d")
        ),
        "comments_count": int(
            selector.css("#js-comments-btn::attr(data-count)").get()
        ),
        "summary": "".join(
            selector.css(".tec--article__body p:first-child *::text").getall()
        ),
        "sources": [
            str(item).strip()
            for item in selector.css("div.z--mb-16 .tec--badge::text").getall()
        ],
        "categories": [
            str(item).strip()
            for item in selector.css(
                "div#js-categories a.tec--badge::text"
            ).getall()
        ],
    }
    return new_dict


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(".tec--list--lg .tec--btn--primary::attr(href)").get()


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
        noticia = scrape_noticia(fetch(url_list[index]))
        noticias.append(noticia)
    create_news(noticias)
    return noticias


