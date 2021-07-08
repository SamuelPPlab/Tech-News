import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    comments_count = selector.css("#js-comments-btn::text").re_first(r"\d+")
    author = selector.css(".tec--author__info__link::text").get()
    new_dict = {
        "url": selector.css("meta[property='og:url']::attr(content)").get(),
        "title": selector.css("#js-article-title::text").get(),
        "timestamp": selector.css("time::attr(datetime)").get(),
        "author": author.strip() if author else author,
        "shares_count": int(shares_count) if shares_count else 0,
        "comments_count": int(comments_count)
        if comments_count
        else comments_count,
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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
