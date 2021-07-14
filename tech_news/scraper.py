import requests
import time
from requests.exceptions import ReadTimeout
from parsel import Selector
import html2text


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
            url, title, timestamp, writer, shares_count,
            comments_count, summary, sources e categories.
    """
    noticia = {}
    selector = Selector(html_content)
    noticia["url"] = selector.css("link[rel='canonical']::attr(href)").get()
    noticia["title"] = selector.css("#js-article-title::text").get()
    noticia["timestamp"] = selector.css("time::attr(datetime)").get()

    writer = selector.css(".tec--author__info__link::text").get().strip()
    noticia["writer"] = None if not writer else writer

    shares_count = int(selector.css(
        ".tec--toolbar__item::text"
    ).get().split()[0])
    noticia["shares_count"] = 0 if not shares_count else shares_count

    noticia["comments_count"] = int(selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get())

    first_paragraph = selector.css(".tec--article__body p").get()
    convert_html2text = html2text.HTML2Text()
    convert_html2text.ignore_links = True
    summary = convert_html2text.handle(first_paragraph).replace("\n", " ")
    noticia["summary"] = summary.replace("  ", "")
    # ref: https://github.com/Alir3z4/html2text/blob/master/docs/usage.md

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
    """Seu código deve vir aqui"""
    # print('URL*******', URL)


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
