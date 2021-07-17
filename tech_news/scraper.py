import requests
import time
from parsel import Selector
from tech_news.database import create_news

# Requisito 1


def fetch(url):
    """Realiza o fetch na URL passada por parametro"""
    time.sleep(1)
    try:
        html = requests.get(url, timeout=3)
    except requests.Timeout:
        return
    if html.status_code != 200:
        return
    return html.text


# Requisito 2
def scrape_noticia(html_content):
    """Recebe um HTML e retorna um dic da notícia"""
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
    """Raspa as noticias"""
    selector = Selector(text=html_content)
    try:
        return selector.css("h3 a.tec--card__title__link::attr(href)").getall()
    except Exception:
        return list()


# Requisito 4
def scrape_next_page_link(html_content):
    """Link para proxima pagina"""
    selector = Selector(text=html_content)
    try:
        return selector.css(".tec--btn ::attr(href)").get()
    except Exception:
        return


# Requisito 5
def get_tech_news(amount):
    """executa a raspagem de dados de X noticias """
    url = "https://www.tecmundo.com.br/novidades"
    noticias = []
    while len(noticias) < amount:
        todas_noticias_pagina = scrape_novidades(fetch(url))
        noticias.extend(todas_noticias_pagina)
        url = scrape_next_page_link(fetch(url))
    amount_noticias = noticias[0:amount]
    lista_noticia_completa = [
        scrape_noticia(fetch(noticia)) for noticia in amount_noticias
    ]
    create_news(lista_noticia_completa)
    return lista_noticia_completa


get_tech_news(20)
