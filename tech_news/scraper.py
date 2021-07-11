import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    writer = selector.css("a.tec--author__info__link::text").get()
    if writer:
        writer = writer.strip()
    shares_count = selector.css("div.tec--toolbar__item::text").get()
    if shares_count:
        shares_count = int((shares_count.strip()).split(" ")[0])
    else:
        shares_count = 0
    comments_count = selector.css("div.tec--toolbar__item::text").get()
    if comments_count:
        comments_count = int((comments_count.strip()).split(" ")[0])
    else:
        comments_count = 0
    summary = "".join(
        selector.css(".tec--article__body p:first-child *::text").getall()
    )
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    sources = [source.strip() for source in sources]
    categories = selector.css("#js-categories a::text").getall()
    categories = [category.strip() for category in categories]

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
    selector = Selector(html_content)
    return selector.css("h3 > .tec--card__title__link::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(".tec--btn::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
