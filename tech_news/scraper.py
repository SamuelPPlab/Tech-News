import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        r = requests.get(url, timeout=3)
        time.sleep(1)

    except requests.ReadTimeout:
        return None

    return r.text if r.status_code == 200 else None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content).css

    url = selector("head link[rel=canonical]::attr(href)").get()

    title = selector(".tec--article__header__title::text").get()

    timestamp = selector("time::attr(datetime)").get()

    writer = selector("a.tec--author__info__link::text").get()

    if writer:
        writer = writer.strip()

    shares_count = selector("div.tec--toolbar__item::text").get()

    if shares_count:
        shares_count = int((shares_count.strip()).split(" ")[0])

    else:
        shares_count = 0

    comments_count = selector("button.tec--btn::attr(data-count)").get()

    if comments_count:
        comments_count = int(comments_count)

    else:
        comments_count = 0
    summary = "".join(
        selector(".tec--article__body > p:first-child *::text").getall()
    )

    sources = selector(".z--mb-16 .tec--badge::text").getall()
    sources = [source.strip() for source in sources]
    categories = selector("#js-categories a::text").getall()
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
    selector = Selector(html_content).css
    return selector("h3 > .tec--card__title__link::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content).css
    return selector(".tec--btn::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    base_url = "https://www.tecmundo.com.br/novidades"

    response_novidades = scrape_novidades(fetch(base_url))
    response_novidades = response_novidades[:amount]

    list_news = [
        scrape_noticia(fetch(base_url)) for base_url in response_novidades
    ]

    create_news(list_news)

    return list_news
