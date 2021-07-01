"""
References:
    https://pypi.org/project/ratelimit/

"""
import requests
from parsel import Selector
from ratelimit import limits, sleep_and_retry


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
    selector = Selector(html_content)
    news["url"] = selector.css(
        "head > meta[property='og:url']::attr(content)"
    ).get()
    news["title"] = selector.css(".tec--article__header__title::text").get()
    news["timestamp"] = selector.css("#js-article-date::attr(datetime)").get()
    news["writer"] = (
        selector.css(".tec--author__info__link::text").get().strip()
    )
    news["shares_count"] = int(
        selector.css(".tec--toolbar__item::text")
        .get()[: -len(shares_count_sufix)]
        .strip()
    )
    news["comments_count"] = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )
    news["summary"] = "".join(
        selector.css(".tec--article__body p:first-child *::text").getall()
    )
    news["sources"] = list(
        map(
            str.strip,
            selector.css(".z--mb-16.z--px-16 .tec--badge::text").getall(),
        )
    )
    news["categories"] = list(
        map(
            str.strip,
            selector.css("#js-categories .tec--badge::text").getall(),
        )
    )
    return news


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
