# Requisito 1
import time
import requests
from parsel import Selector

# import time


def fetch(url):
    try:

        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:

        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    sources = [
        item.strip()
        for item in selector.css(".z--mb-16 div a.tec--badge::text").getall()
    ]

    categories = [
        category.strip()
        for category in selector.css(
            "#js-categories .tec--badge::text"
        ).getall()
    ]

    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count:
        shares_count = int((shares_count.strip()).split(" ")[0])
    else:
        shares_count = 0
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments_count:
        comments_count = int((comments_count))
    else:
        comments_count = 0

    summary = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )
    url = selector.css("head > meta[property='og:url']::attr(content)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get()
    if writer:
        writer = writer.strip()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
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
