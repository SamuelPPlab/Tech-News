import requests
import time
from requests.exceptions import ReadTimeout
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Faz requisição HTTP a um site e retorna seu conteúdo HTML"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
    except ReadTimeout:
        None


# Requisito 2
def scrape_noticia(html_content):
    """
        Recebe um conteúdo HTML e retorna um dict com as informações:
            - url, title, timestamp, writer, shares_count,
            comments_count, summary, sources e categories.
    """
    noticia = {}
    selector = Selector(html_content)
    noticia["url"] = selector.css("link[rel='canonical']::attr(href)").get()
    noticia["title"] = selector.css("#js-article-title::text").get()
    noticia["timestamp"] = selector.css("time::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get()
    writer = writer.strip() if writer else None
    noticia["writer"] = None if not writer else writer

    shares_count = selector.css(".tec--toolbar__item::text").get()
    shares_count = int(shares_count.split()[0]) if shares_count else None
    noticia["shares_count"] = 0 if not shares_count else shares_count

    comments_count = selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get()
    # noticia["comments_count"] = int(
    # comments_count) if comments_count else None
    noticia["comments_count"] = int(
        comments_count) if comments_count is not None else 0

    first_paragraph = selector.css(
        "div.tec--article__body > p:first-child ::text"
    ).getall()
    summary = "".join(first_paragraph)
    noticia["summary"] = summary

    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    noticia["sources"] = [source.strip() for source in sources]

    categories = selector.css("#js-categories .tec--badge::text").getall()
    noticia["categories"] = [category.strip() for category in categories]
    return noticia


# Requisito 3
def scrape_novidades(html_content):
    """
        - Recebe uma string com conteúdo HTML,
        - Faz o scrape de seu conteúdo,
        - Retorna uma lista contendo as URLs das notícias listadas.
    """

    selector = Selector(html_content)
    URL_list = selector.css(
        "h3 > .tec--card__title__link::attr(href)"
    ).getall()
    return URL_list


# Requisito 4
def scrape_next_page_link(html_content):
    """
        - Recebe uma string com um conteúdo HTML
        - Faz o scrape deste HTML para obter a URL da próxima página
        - Retorna a URL obtida
    """

    selector = Selector(html_content)
    URL = selector.css(
        ".tec--btn::attr(href)"
    ).get()
    return URL


# Requisito 5
def get_tech_news(amount: int) -> list[str]:
    """
        - Recebe um número e retorna essa quantidade de noticias
        - Insere essas notícias no MongoDB
        - Retorna as notícias inseridas no DB
    """
    # Ref: Desenvolvido com ajuda da Lorena Goes

    url = 'https://www.tecmundo.com.br/novidades'
    all_news_list = []
    while len(all_news_list) <= amount:
        request = fetch(url)
        for endpoint in scrape_novidades(request):
            all_news_list.append(scrape_noticia(fetch(endpoint)))
            if len(all_news_list) == amount:
                create_news(all_news_list)
                return all_news_list
            url = scrape_next_page_link(request)
