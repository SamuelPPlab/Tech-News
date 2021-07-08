import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None

    time.sleep(1)

    if response.ok:
        return response.text
    else:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)

    return {
        "url": selector.css("head > link:nth-child(26)").css("link::attr(href)").get(),
        "title": selector.css("h1::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": selector.css("#js-author-bar div p a::text").get().strip(),
        "shares_count": int(selector.css("#js-author-bar nav div::text").get().split()[0]),
        "comments_count": int(selector.css("#js-author-bar nav div button::attr(data-count)").get()),
        "summary": ''.join(selector.css(".tec--article__body p:nth-child(1) *::text").getall()),
        "sources": [source.strip() for source in selector.css(".z--mb-16 div a::text").getall()],
        "categories": [category.strip() for category in selector.css("#js-categories a::text").getall()],
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
