import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    noticia = {}
    noticia["url"] = selector.css(
        "head > link[rel='canonical']::attr(href)"
    ).get()
    noticia["title"] = selector.css(".tec--article__header__title::text").get()
    noticia["timestamp"] = selector.css("time::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get()
    if writer is not None:
        noticia["writer"] = writer.strip()
    shares = selector.css(".tec--toolbar__item::text").get()
    if shares is not None:
        noticia["shares_count"] = int(shares[1:2])
    else:
        noticia["shares_count"] = 0
    comments_count = selector.css(".tec--btn::attr(data-count)").get()
    if comments_count is not None:
        noticia["comments_count"] = int(comments_count)
    else:
        noticia["comments_count"] = 0
    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    noticia["summary"] = "".join(summary)
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    for i in range(len(sources)):
        sources[i] = sources[i].strip()
    noticia["sources"] = sources
    categories = selector.css("#js-categories > a::text").getall()
    for i in range(len(categories)):
        categories[i] = categories[i].strip()
    noticia["categories"] = categories
    return noticia


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    novidades_url = []
    for urls in selector.css(".tec--list.tec--list--lg .tec--list__item"):
        novidades_url.append(urls.css("a::attr(href)").get())
    return novidades_url


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css("head link[rel='next']::attr(href)").get()
    return next_page_link


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    all_news = []
    novidades_url = scrape_novidades(fetch(url))
    for i in range(amount):
        if len(novidades_url) == 0:
            url = scrape_next_page_link(fetch(url))
            novidades_url = scrape_novidades(fetch(url))

        all_news.append(scrape_noticia(fetch(novidades_url[0])))
        novidades_url.pop(0)
    create_news(all_news)
    return all_news


# get_tech_news(25)
