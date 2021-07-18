from parsel import Selector
import requests
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    data = {}
    data["url"] = selector.css("head link[rel=canonical]::attr(href)").get()
    data["title"] = selector.css(".tec--article__header__title::text").get()
    data["timestamp"] = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    data["writer"] = (
        selector.css(".tec--author__info__link::text").get().strip()
    )
    shares = selector.css(".tec--toolbar__item::text").get().strip().split()
    data["shares_count"] = int(shares[0])
    data["comments_count"] = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )
    summary = selector.css(
        ".tec--article__body p:first-child *::text"
    ).getall()
    data["summary"] = "".join(summary)
    sources = selector.css(".z--mb-16 div a::text").getall()
    sources = [source.strip() for source in sources]
    categories = selector.css("#js-categories a::text").getall()
    categories = [category.strip() for category in categories]
    data["sources"] = sources
    data["categories"] = categories
    print(data)
    return data


# Requisito 3
def scrape_novidades(html_content):
    try:
        selector = Selector(html_content)
        links = selector.css("h3 a::attr(href)").getall()
        return links
    except Exception:
        list()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    nextPage = selector.css(".tec--btn::attr(href)").get()
    return nextPage


# Requisito 5
def get_tech_news(amount):
    tecmundoUrl = "https://www.tecmundo.com.br/novidades"
    noticiasNovidades = scrape_novidades(fetch(tecmundoUrl))
    print(len(noticiasNovidades))
    noticiasNovidades = noticiasNovidades[0:amount]
    print(len(noticiasNovidades))
    noticias = [
        scrape_noticia(fetch(noticiaUrl)) for noticiaUrl in noticiasNovidades
    ]
    create_news(noticias)
    return noticias


get_tech_news(5)
