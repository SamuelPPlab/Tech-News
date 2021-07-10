import requests
import time
import math
from parsel import Selector


from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except Exception as e:
        print("Error exception: ", e)
        return None
    else:
        return response.text


# Requisito 2
def scrape_noticia(html_content):
    noticia = {}
    selector = Selector(text=html_content)
    noticia['url'] = selector.css("link[ rel=canonical] ::attr(href)").get()
    noticia['title'] = selector.css("#js-article-title::text").get()
    noticia['timestamp'] = selector.css(
        "#js-article-date ::attr(datetime)").get()
    noticia['writer'] = (selector.css(
        ".tec--author__info__link::text").get().strip()
        if selector.css(".tec--author__info__link::text").get() else None)
    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count:
        noticia['shares_count'] = int(shares_count.split()[0])
    else: 
        noticia['shares_count'] = 0
    comments_count = selector.css("#js-comments-btn ::attr(data-count)").get()
    if comments_count:
        noticia['comments_count'] = int(comments_count.split()[0])
    else: 
        noticia['comments_count'] = 0
    noticia['summary'] = "".join(selector.css(
        ".tec--article__body > p:first-child *::text").getall())
    noticia['sources'] = list(map(str.strip, selector.css(
        ".z--mb-16 .tec--badge::text").getall()))
    noticia['categories'] = list(map(str.strip, selector.css(
        "#js-categories a ::text").getall()))

    return {
        "url": noticia['url'],
        "title":  noticia['title'] ,
        "timestamp": noticia['timestamp'],
        "writer": noticia['writer'] ,
        "shares_count": noticia['shares_count'],
        "comments_count":  noticia['comments_count'] ,
        "summary":  noticia['summary'] ,
        "sources":  noticia['sources'] ,
        "categories": noticia['categories']
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css("h3 a ::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(".tec--list > a ::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    URL = "https://www.tecmundo.com.br/novidades"
    NEWS = []
    LINK_NEWS = []
    for _ in range(math.ceil(amount / 20)):
        HTML_CONTENT = fetch(URL)
        scrape_news = scrape_novidades(HTML_CONTENT)
        for link_url in scrape_news:
            LINK_NEWS.append(link_url)
        URL = scrape_next_page_link(HTML_CONTENT)

    for item in range(amount):
        NEWS.append(scrape_noticia(fetch(LINK_NEWS[item])))

    create_news(NEWS)
    return NEWS
