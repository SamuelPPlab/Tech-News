import requests
import time
from parsel import Selector

from tech_news.database import (
    create_news,
)


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
    except (
        requests.exceptions.RequestException,
        requests.exceptions.HTTPError,
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
    ):
        return None

    time.sleep(1)

    if response.status_code != 200:
        return None

    return response.text


# Requisito 2
def scrape_noticia(html_content):
    noticia = {}
    selector = Selector(text=html_content)

    noticia["url"] = selector.css(
        "meta[property='og:url']::attr(content)"
    ).get()

    noticia["title"] = selector.css("#js-article-title::text").get().strip()

    noticia["timestamp"] = (
        selector.css("#js-article-date ::attr(datetime)").get().strip()
    )

    if selector.css(".tec--author__info__link::text").get() is None:
        noticia["writer"] = None
    else:
        noticia["writer"] = (
            selector.css(".tec--author__info__link::text").get().strip()
        )

    if selector.css(".tec--toolbar__item::text").get() is None:
        noticia["shares_count"] = 0
    else:
        noticia["shares_count"] = int(
            selector.css(".tec--toolbar__item::text").get().strip()[:2]
        )

    if selector.css("#js-comments-btn::attr(data-count)").get() is None:
        noticia["comments_count"] = 0
    else:
        noticia["comments_count"] = int(
            selector.css("#js-comments-btn::attr(data-count)").get()
        )

    noticia["summary"] = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )

    noticia["sources"] = [
        source.strip()
        for source in selector.css(".z--mb-16 div a.tec--badge::text").getall()
    ]

    noticia["categories"] = [
        category.strip()
        for category in selector.css(
            "#js-categories .tec--badge::text"
        ).getall()
    ]
    return noticia


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    return selector.css("h3 .tec--card__title__link::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    next_page_url = selector.css(".tec--btn::attr(href)").get()

    return next_page_url


# print(scrape_next_page_link(fetch("https://www.tecmundo.com.br/novidades")))

# Requisito 5
# def get_tech_news(amount):
#     URL_BASE = "https://www.tecmundo.com.br/novidades"
#     # count = 0
#     listaNoticias = []

#     for i in range(math.ceil(amount / 20)):
#         # html_content = fetch(URL_BASE)
#         # selector = Selector(text=html_content)

#         for i in range(19):
#             listaUrls = scrape_novidades(fetch(URL_BASE))
#             noticia = scrape_noticia(fetch(listaUrls[i]))
#             listaNoticias.append(noticia)
#             if i == amount - 1:
#                 break

#         URL_BASE = scrape_next_page_link(fetch(URL_BASE))
#         # if count == amount:
#         #     break

#     create_news(listaNoticias)
#     return find_news()


def get_tech_news(amount):
    URL_BASE = "https://www.tecmundo.com.br/novidades"
    listaDeNoticias = []

    html = fetch(URL_BASE)

    while len(listaDeNoticias) < amount:
        listaDeNoticias.extend(
            [
                scrape_noticia(fetch(tech_news))
                for tech_news in scrape_novidades(html)
            ]
        )
        if len(listaDeNoticias) < amount:
            html = fetch(scrape_next_page_link(html))

    create_news(listaDeNoticias[:amount])
    return listaDeNoticias[:amount]
