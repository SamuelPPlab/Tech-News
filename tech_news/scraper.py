import requests
import time
from parsel import Selector


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
    data = {
        "url": selector.css("meta[property='og:url']::attr(content)").get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": selector.css(".tec--author__info__link::text").get().strip(),
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
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


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css("h3 > a.tec--card__title__link::attr(href)").getall()


# print(scrape_novidades(fetch("https://www.tecmundo.com.br/novidades")))


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(
        "a.tec--btn::attr(href)"
    ).get()


# print(scrape_next_page_link(fetch("https://www.tecmundo.com.br/novidades")))


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
