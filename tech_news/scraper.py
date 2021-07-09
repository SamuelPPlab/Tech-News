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
    seletor = Selector(html_content)
    shares_count = seletor.css(
        "#js-author-bar > nav > div:nth-child(1)::text"
    ).get()
    comments_count = seletor.css("#js-comments-btn::attr(data-count)").get()
    writer = seletor.css(
        "#js-author-bar > div > p.z--m-none.z--truncate.z--font-bold > a::text"
    ).get()
    return {
        "url": seletor.css('head > link[rel="canonical"]::attr(href)').get(),
        "title": seletor.css("#js-article-title::text").get(),
        "timestamp": seletor.css("#js-article-date::attr(datetime)").get(),
        "writer": writer.strip() if writer is not None else None,
        "shares_count": int(shares_count.split()[0])
        if shares_count is not None
        else 0,
        "comments_count": int(comments_count) if comments_count is not None
        else 0,
        "summary": "".join(
            seletor.css(
                ".tec--article__body > p:nth-child(1) *::text"
            ).getall()
        ),
        "sources": [
            fonte.strip()
            for fonte in seletor.css(
                ".tec--article__body-grid > " +
                "div:nth-last-child(2) > div > a *::text"
            ).getall()
        ],
        "categories": [
            categoria.strip()
            for categoria in seletor.css(
                ".tec--article__body-grid > " +
                "div:nth-last-child(1) > div > a *::text"
            ).getall()
        ],
    }


# Requisito 3
def scrape_novidades(html_content):
    seletor = Selector(html_content)
    lista = seletor.css("h3.tec--card__title > a::attr(href)").getall()
    if len(lista) == 0:
        return []
    return lista


# Requisito 4
def scrape_next_page_link(html_content):
    seletor = Selector(html_content)
    return seletor.css("div.tec--list > a:last-child::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    bruto = fetch(url)
    next_link = scrape_next_page_link(bruto)
    lista_link = scrape_novidades(bruto)
    lista_noticias = []
    while len(lista_link) < amount:
        new_bruto = fetch(next_link)
        lista_link += scrape_novidades(new_bruto)
        next_link = scrape_next_page_link(new_bruto)
        print(len(lista_link))
    for num in range(0, amount):
        print(lista_link[num])
        new_bruto = fetch(lista_link[num])
        noticia = scrape_noticia(new_bruto)
        lista_noticias.append(noticia)
    create_news(lista_noticias)
    return lista_noticias
