import requests
from time import sleep
from parsel import Selector
from tech_news.database import create_news

# Requisito 1


# def fetch(url):
#     try:
#         if (url == ''):
#             return None
#         response = requests.get(url, timeout=3)
#         time.sleep(1)
#         if response.status_code != 200:
#             return None
#         return response.text
#     except requests.ReadTimeout:
#         return None


# Requisito 1


def fetch(url):
    try:
        sleep(1)
        requests.encoding = "utf-8"
        response = requests.get(url, timeout=3)
        return response.text if response.status_code == 200 else None
    except requests.Timeout:
        return None


# Requisito 2


def scrape_noticia(html_content):

    newsList = {}

    selector = Selector(html_content)

    newsList["url"] = selector.css("head > \
    meta[property='og:url']::attr(content)").get()

    newsList["title"] = selector.css("#js-article-title::text").get()

    writer = selector.css(".tec--author__info__link::text").get()

    if writer:
        writer = writer.strip()

    newsList["writer"] = writer

    shares_count = selector.css("#js-author-bar > nav > div::text").get()

    if shares_count:
        shares_count = int(
            shares_count.replace(" ", "").replace("Compartilharam", "")
        )
    else:
        shares_count = 0

    newsList["shares_count"] = shares_count

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()

    if comments_count:
        comments_count = int(comments_count)
    elif comments_count is None:
        comments_count = 0

    newsList["comments_count"] = comments_count

    summary = selector.css(
        "div.tec--article__body > p:first-child *::text"
    ).getall()

    summary = "".join(summary)

    newsList["summary"] = summary

    newsList["categories"] = list(
        map(str.strip, selector.css("#js-categories > a::text").getall())
    )

    newsList["sources"] = list(
        map(
            str.strip,
            selector.css("a[class=tec--badge]::text").getall(),
        )
    )

    newsList["timestamp"] = selector.css("\
        #js-article-date::attr(datetime)").get()

    return newsList


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    list = selector.css("h3 > a::attr(href)").getall()
    return list


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 \
    > div.tec--list.tec--list--lg > a::attr(href)"
    ).get()
    return next_page


# Requisito 5
def get_tech_news(amount):
    restante = amount
    url = "https://www.tecmundo.com.br/novidades"
    noticias = scrape_novidades(fetch(url))
    mongoappend = []
    for noticia in noticias:
        conteudo = fetch(noticia)
        mongo = scrape_noticia(conteudo)
        mongoappend.append(mongo)
    restante = restante - 20
    while restante > 0:
        next_page = scrape_next_page_link(fetch(url))
        noticias = scrape_novidades(fetch(next_page))
        for noticia in noticias:
            conteudo = fetch(noticia)
            mongo = scrape_noticia(conteudo)
            mongoappend.append(mongo)
        url = next_page
        restante = restante - 20

    while len(mongoappend) > amount:
        pos = len(mongoappend) - 1
        del mongoappend[pos]

    create_news(mongoappend)
    return mongoappend
