import requests
import parsel
from time import sleep
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        sleep(1)
        response = requests.get(url, timeout=3)
        return response.text if response.status_code == 200 else None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):

    selector = Selector(html_content)
    noticia = {}
    noticia["url"] = selector.css("link[rel='canonical']::attr(href)").get()
    noticia["title"] = selector.css(".tec--article__header__title::text").get()
    noticia["timestamp"] = selector.css("time::attr(datetime)").get()
    try:
        writer = selector.css(".tec--author__info__link::text").get()
        noticia["writer"] = writer.strip()
    except AttributeError:
        noticia["writer"] = None
    try:
        shares_count = selector.css(".tec--toolbar__item::text").get()
        noticia["shares_count"] = int(shares_count.split()[0])
    except AttributeError:
        noticia["shares_count"] = 0
    noticia["comments_count"] = (
        int(selector.css(".tec--btn::attr(data-count)").get()) or 0
    )

    noticia["summary"] = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )

    noticia["sources"] = list(
        map(str.strip, selector.css(".z--mb-16 .tec--badge::text").getall())
    )
    categories = selector.css("#js-categories a::text").getall()
    noticia["categories"] = list(map(str.strip, categories))
    return noticia


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    URL = selector.css("h3 > .tec--card__title__link::attr(href)").getall()
    return URL


# Requisito 4
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    url = selector.css("a.tec--btn::attr(href)").get()
    return url or None


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    news = []
    quantity = int(amount)

    while len(news) < quantity:
        html_content = fetch(url)
        news.extend(scrape_novidades(html_content))
        url = scrape_next_page_link(html_content)

    newsSplice = news[:quantity]
    newsList = []
    for url in newsSplice:
        html_content = fetch(url)
        newsList.append(scrape_noticia(html_content))

    try:
        create_news(newsList)
    except Exception as e:
        print(e)

    return newsList
