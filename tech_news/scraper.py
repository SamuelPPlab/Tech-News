import requests
import time
from parsel import Selector


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

    url = selector("meta[property='og:url']::attr(content)").get()

    title = selector("#js-article-title::text").get()

    timestamp = selector("#js-article-date ::attr(datetime)").get()

    writer = selector(".tec--author__info__link::text").get()

    if writer:
        writer = writer.strip()

    shares_count = selector(".tec--toolbar__item::text").get()

    if shares_count:
        shares_count = int((shares_count.strip()).split(" ")[0])

    else:
        shares_count = 0
    comments_count = selector(".tec--toolbar__item::text").get()

    if comments_count:
        comments_count = int((comments_count.strip()).split(" ")[0])

    else:
        comments_count = 0
    summary = "".join(
        selector(".tec--article__body p:first-child *::text").getall()
    )

    sources = selector(".z--mb-16 .tec--badge::text").getall()
    sourcesA = [source.strip() for source in sources]
    categories = selector("#js-categories a::text").getall()
    categoriesA = [category.strip() for category in categories]

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sourcesA,
        "categories": categoriesA,
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
