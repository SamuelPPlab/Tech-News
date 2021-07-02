import requests
import time
from parsel import Selector
import pprint


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news_letter = {}
    news_letter["url"] = selector.css(
        "head > meta[property='og:url']::attr(content)"
    ).get()
    news_letter["title"] = selector.css("#js-article-title::text").get()
    news_letter["timestamp"] = selector.css(
        "#js-article-date::attr(datetime)"
    ).get()
    news_letter["writer"] = (
        selector.css(".tec--author__info__link::text").get().strip()
    )
    news_letter["shares_count"] = int(
        selector.css(".tec--toolbar__item::text")
        .get()[: -len("Compartilharam")]
        .strip()
    )
    news_letter["comments_count"] = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )
    news_letter["summary"] = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )
    news_letter["sources"] = list(
        map(
            str.strip,
            selector.css(".z--mb-16 div a.tec--badge::text").getall(),
        )
    )
    news_letter["categories"] = list(
        map(
            str.strip,
            selector.css("#js-categories a.tec--badge::text").getall(),
        )
    )

    return news_letter


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    response = selector.css(
        "h3 > .tec--card__title__link::attr(href)"
    ).getall()

    return response


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    response = selector.css(
        ".tec--btn::attr(href)"
    ).get()

    return response


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


pp = pprint.PrettyPrinter(indent=4)
fetched_data = fetch("https://www.tecmundo.com.br/novidades")
pp.pprint(scrape_next_page_link(fetched_data))
# pp.pprint(scrape_novidades(fetched_data))
