import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        sleep(1)
        if response.status_code != 200:
            raise Exception("Error during request")
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    selectors = {
        "url": "meta[property='og:url']::attr(content)",
        "title": "#js-article-title::text",
        "timestamp": "time#js-article-date::attr(datetime)",
        "writer": "a.tec--author__info__link::text",
        "shares_count": ".tec--toolbar__item::text",
        "comments_count": "button#js-comments-btn::attr(data-count)",
        "summary": "div.tec--article__body p:first-of-type *::text",
        "sources": ".z--mb-16 a::text",
        "categories": "#js-categories a::text",
    }

    return {
        "url": selector.css(selectors["url"]).get(),
        "title": selector.css(selectors["title"]).get(),
        "timestamp": selector.css(selectors["timestamp"]).get(),
        "writer": selector.css(selectors["writer"]).get(),
        "shares_count": [
            int(s)
            for s in selector.css(selectors["shares_count"]).get().split(" ")
            if s.isdigit()
        ][0],
        "comments_count": int(selector.css(selectors["comments_count"]).get()),
        "summary": "".join(selector.css(selectors["summary"]).getall()),
        "sources": selector.css(selectors["sources"]).getall(),
        "categories": selector.css(selectors["categories"]).getall(),
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
