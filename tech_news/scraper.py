import requests
import time
from parsel import Selector
from tech_news.database import create_news
import math
# Requisito 1


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    # https://stackoverflow.com/questions/28377421/why-do-i-receive-a-timeout-error-from-pythons-requests-module
    except requests.ReadTimeout:
        return None
    if response.status_code != 200:
        return None
    return response.text

# Requisito 2


def scrape_noticia(html_content):
    # https://www.tecmundo.com.br/dispositivos-moveis/215327-pixel-5a-tera-lancamento-limitado-devido-escassez-chips.htm

    selector = Selector(html_content)
    url = selector.xpath("*//link/@href").getall()[20]
    # print(selector.xpath("*//link/@href").getall()[20])

    title = selector.css(".tec--article__header__title::text").get()
    # print(selector.css(".tec--article__header__title::text").get())

    timestamp = selector.css("time ::attr(datetime)").get()
    # print(selector.css("time ::attr(datetime)").get())
    # try:
    writer = selector.css("a.tec--author__info__link::text").get()
    #     if writer is None:
    #         print("Reclamando que não pode retirar vazio de objeto nulo")
    # except AttributeError:
    #     writer = " valor nulo "
    # retirar espaços em branco
    # https://www.delftstack.com/pt/howto/python/how-to-remove-whitespace-in-a-string/
    # print(selector.css("a.tec--author__info__link::text").get())
    # try:
    shares_count = int(selector.css(".tec--toolbar__item::text").re_first(
        r"\d+"))
    #     if shares_count is not None:
    #         print("nada é alguma coisa em python")
    # except TypeError:
    #     shares_count = "valor nulo"
    # cast para int
    # print(shares_count = selector.css(".tec--toolbar__item::text").re_first(
    # r"\d+"))

    # summary_concat = ''; #o código de baixo é mais limpo
    # for value in selector.css(".tec--article__body >p:first-child ::text")
    #   .getall():
    #     summary_concat += value
    # print(selector.css(".tec--article__body >p:first-child ::text").getall())

    summary = ''.join(
        selector.css(
            ".tec--article__body >p:first-child ::text"
            ).getall())

    comments_count = int(selector.css(
        "div.tec--toolbar__item ::text").re_first(r"\d+"))
    # print(selector.css("div.tec--toolbar__item ::text").re_first(r"\d+"))

    sources = selector.css("div.z--mb-16 .tec--badge::text").getall()
    # retirar espaços em branco
    # print(selector.css("div.z--mb-16 .tec--badge::text").getall())

    categories = selector.css("#js-categories .tec--badge ::text").getall()
    # retirar espaços em branco
    # print(selector.css("#js-categories .tec--badge ::text").getall())

    data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer.strip() if writer else "valor nulo",
        "shares_count": shares_count if shares_count else 0,
        "comments_count": comments_count if comments_count else 0,
        "summary": summary,
        "sources": list(map(lambda source: source.strip(), sources)),
        "categories": list(map(lambda category: category.strip(), categories))
    }
    return data

# Requisito 3


def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css("h3 > a.tec--card__title__link::attr(href)").getall()


# Requisito 4


def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css("a.tec--btn::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    news = []
    url_list = []
    url = "https://www.tecmundo.com.br/novidades"
    for _ in range(math.ceil(amount / 20)):
        time.sleep(0.1)
        html_content = fetch(url)
        news_link_list = scrape_novidades(html_content)
        for url_link in news_link_list:
            url_list.append(url_link)
            url = scrape_next_page_link(html_content)
    for index in range(amount):
        news.append(scrape_noticia(fetch(url_list[index])))
    print(url_list)
    create_news(news)
    return news
