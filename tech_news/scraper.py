import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        print(response)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = (
        selector.css(".tec--author__info__link::text").get().strip()
        if selector.css(".tec--author__info__link::text").get() else None
    )
    shares_count = int(selector.css(".tec--toolbar__item::text").get()[1:2])
    comments_count = int(selector.css(".tec--btn::attr(data-count)").get())
    summary = "".join(selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall())
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    for i in range(len(sources)):
        sources[i] = sources[i].strip()
    categories = selector.css("#js-categories .tec--badge::text").getall()
    for i in range(len(categories)):
        categories[i] = categories[i].strip()
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
    selector = Selector(html_content)
    lista = selector.css(".tec--card__info h3 a::attr(href)").getall()
    return lista


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    lista = (
        selector.css(".tec--btn::attr(href)").get()
        if selector.css(".tec--btn::attr(href)").get()
        else None
    )

    return lista


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
