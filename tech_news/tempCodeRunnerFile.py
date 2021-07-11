import requests
import time
from parsel import Selector


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

    noticia["timestamp"] = selector.css(
        "#js-article-date ::attr(datetime)"
    ).get()

    noticia["writer"] = (
        selector.css(".tec--author__info__link::text").get().strip()
    )

    if selector.css(".tec--toolbar__item::text").get() is None:
        noticia["shares_count"] = 0
    noticia["shares_count"] = int(
        selector.css(".tec--toolbar__item::text").get().strip()[0]
    )

    if selector.css("#js-comments-btn::attr(data-count)").get() is None:
        noticia["comments_count"] = 0
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
    print(noticia)


string1 = "https://www.tecmundo.com.br/dispositivos-moveis/215327"
string2 = "-pixel-5a-tera-lancamento-limitado-devido-escassez-chips.htm"
scrape_noticia(fetch(string1 + string2))
