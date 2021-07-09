import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)

    except requests.ReadTimeout:
        return None

    return response.text if response.status_code == 200 else None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    data = {}
    data["url"] = selector.css("head link[rel=canonical]::attr(href)").get()
    data["title"] = selector.css("#js-article-title::text").get()
    data["timestamp"] = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css( 
        ".tec--author__info__link::text"
    ).get()
    data['writer'] = writer.strip() if writer else None
    shares_count = selector.css(
        ".tec--toolbar__item::text"
    ).get()
    data['shares_count'] = int(shares_count.split()[0]) if shares_count else 0
    comments_count = selector.css("#js-comments-btn::text").re_first(r"\d+")
    data['comments_count'] = int(comments_count) if comments_count else 0
    data['summary'] = "".join(selector.css(
        ".tec--article__body p:nth-child(1) *::text"
    ).getall())
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    data['sources'] = [source.strip() for source in sources]
    categories = selector.css("#js-categories > a *::text").getall()
    data['categories'] = [category.strip() for category in categories]
    return data


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
