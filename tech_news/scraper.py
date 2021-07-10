import requests
import time
from parsel import Selector

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
    noticia['timestamp'] = selector.css("#js-article-date ::attr(datetime)").get()
    noticia['writer'] = (selector.css(".tec--author__info__link::text").get().strip() if selector.css(".tec--author__info__link::text").get() else None)
    noticia['shares_count'] = int((selector.css(".tec--toolbar__item::text").get()).split()[0])
    noticia['comments_count'] = int(selector.css("#js-comments-btn ::attr(data-count)").get())
    noticia['summary'] = "".join(selector.css(".tec--article__body > p:first-child *::text").getall())
    noticia['sources'] = list(map(str.strip, selector.css(".z--mb-16 .tec--badge::text").getall()))
    noticia['categories'] = list(map(str.strip, selector.css("#js-categories a ::text").getall()))
    return noticia


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
