import time
import requests
import parsel
from tech_news.database import insert_or_update

LINK_NOVIDADES = "https://www.tecmundo.com.br/novidades"


def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    if(response.status_code == 200):
        return response.text
    else:
        return None


def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    response = {}
    response["url"] = selector.css(
        "head > meta[property='og:url']::attr(content)"
    ).get()
    response["title"] = selector.css("#js-article-title::text").get()
    response["timestamp"] = selector.css(
        "#js-article-date::attr(datetime)"
    ).get()
    response["writer"] = selector.css(
        ".tec--author__info__link::text"
    ).get().strip()
    response["shares_count"] = int(
        selector.css(".tec--toolbar__item::text")
        .get()[: -len("Compartilharam")]
        .strip()
    )
    response["comments_count"] = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )
    response["summary"] = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )
    response["sources"] = list(
        map(
            str.strip,
            selector.css(".z--mb-16 div a.tec--badge::text").getall(),
        )
    )
    response["categories"] = list(
        map(
            str.strip,
            selector.css("#js-categories a.tec--badge::text").getall(),
        )
    )
    return response


def scrape_novidades(html_content):
    return parsel.Selector(html_content).css(
        "h3 > a.tec--card__title__link::attr(href)"
        ).getall()


def scrape_next_page_link(html_content):
    return parsel.Selector(html_content).css(
        "div.tec--list > a:last-child::attr(href)"
    ).get()


def get_tech_news(amount):
    url = LINK_NOVIDADES
    response = []

    for i in range(1, amount):
        new = scrape_noticia(fetch(url))
        response.append(new)
        insert_or_update(new)
        url = scrape_next_page_link(fetch(url))
    return response
