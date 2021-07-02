"""
References:
    https://pypi.org/project/ratelimit/

"""
import requests
from parsel import Selector
from ratelimit import limits, sleep_and_retry
from tech_news.database import create_news


# Requisito 1
@sleep_and_retry
@limits(calls=1, period=1)  # 1 cal / 1 sec
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except (
        requests.exceptions.RequestException,
        requests.exceptions.HTTPError,
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
    ) as err:
        print("Exception on fetch: ", err)
        return None
    else:
        return response.text


# Requisito 2
def scrape_noticia(html_content):
    news = {}
    shares_count_sufix = "Compartilharam"
    selector = Selector(text=html_content)
    news["url"] = selector.css(
        "head > meta[property='og:url']::attr(content)"
    ).get()
    news["title"] = selector.css(".tec--article__header__title::text").get()
    news["timestamp"] = selector.css("#js-article-date::attr(datetime)").get()
    news["writer"] = (
        selector.css(".tec--author__info__link::text").get().strip()
        if selector.css(".tec--author__info__link::text").get() is not None
        else None
    )
    news["shares_count"] = int(
        selector.css(".tec--toolbar__item::text")
        .get()[: -len(shares_count_sufix)]
        .strip()
        if selector.css(".tec--toolbar__item::text").get() is not None
        else 0
    )
    news["comments_count"] = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
        if selector.css("#js-comments-btn::attr(data-count)").get() is not None
        else 0
    )
    news["summary"] = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )
    news["sources"] = [
        source.strip()
        for source in selector.css(".z--mb-16 div a.tec--badge::text").getall()
    ]
    news["categories"] = [
        category.strip()
        for category in selector.css(
            "#js-categories .tec--badge::text"
        ).getall()
    ]

    return news


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(
        "div.tec--list.tec--list--lg a.tec--btn--primary::attr(href)"
    ).get()


# Requisito 5
def get_tech_news(amount):
    URL_TECH_NEWS = "https://www.tecmundo.com.br/novidades"
    result = []

    page_tech_news = fetch(URL_TECH_NEWS)

    while len(result) < amount:
        result.extend(
            [
                scrape_noticia(fetch(tech_news))
                for tech_news in scrape_novidades(page_tech_news)
            ]
        )
        if len(result) < amount:
            page_tech_news = fetch(scrape_next_page_link(page_tech_news))

    create_news(result[:amount])
    return result[:amount]