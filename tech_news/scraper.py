import time
import requests
import parsel
from tech_news.database import create_news
# peguei ideia de validação da busca no PR do Zezo

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
    response["writer"] = (
        selector.css(".tec--author__info__link::text").get().strip()
        if selector.css(".tec--author__info__link::text").get() is not None
        else None
    )
    response["shares_count"] = int(
        selector.css(".tec--toolbar__item::text")
        .get()
        .strip()[: -len("Compartilharam")]
        if selector.css(".tec--toolbar__item::text").get() is not None
        else 0
    )
    response["comments_count"] = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
        if selector.css("#js-comments-btn::attr(data-count)").get() is not None
        else 0
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
    page = fetch(LINK_NOVIDADES)
    links = []
    news = []
    while len(links) < amount:
        next_page = scrape_next_page_link(page)
        response = scrape_novidades(page)
        links.extend(response)
        if len(links) < amount:
            page = fetch(next_page)

    for link in links:
        news_data = scrape_noticia(fetch(link))
        news.append(news_data)

    create_news(news[:amount])
    return news[:amount]
