# Requisito 1
import requests
import time
from parsel import Selector
from tech_news.database import create_news


def fetch(url):
    time.sleep(1)
    response = ""
    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
    except requests.ReadTimeout:
        return None

    return response.text


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    dict_news = {}

    dict_news["url"] = selector.css(
        "head > meta[property='og:url']::attr(content)"
    ).get()

    dict_news["title"] = selector.css(
        ".tec--article__header__title::text"
    ).get()

    dict_news["timestamp"] = selector.css(
        "#js-article-date::attr(datetime)"
    ).get()

    writer = selector.css(".tec--author__info__link::text").get()
    dict_news["writer"] = writer.strip() if writer else None

    shares_count = selector.css(".tec--toolbar__item::text").get()
    dict_news["shares_count"] = (
        int(shares_count.split()[0]) if shares_count else 0
    )

    comments_count = selector.css(
        ".tec--toolbar__item #js-comments-btn::attr(data-count)"
    ).get()
    dict_news["comments_count"] = int(comments_count) if comments_count else 0

    dict_news["summary"] = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )

    dict_news["sources"] = [
        source.strip()
        for source in selector.css(".z--mb-16 div a.tec--badge::text").getall()
    ]

    dict_news["categories"] = [
        category.strip()
        for category in selector.css(
            "#js-categories .tec--badge::text"
        ).getall()
    ]

    return dict_news


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)

    list_urls = selector.css(
        ".tec--list--lg .tec--card__info h3 a::attr(href)"
    ).getall()

    return list_urls


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    url_page = True

    while url_page:
        url_page = selector.css(".tec--btn::attr(href)").get()
        return url_page

        selector = Selector(fetch(url_page))

    return None


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    news_db = []
    while url:
        response = fetch(url)
        url_list = scrape_novidades(response)
        for news_list in url_list:
            response_news = fetch(news_list)
            new_news = scrape_noticia(response_news)
            news_db.append(new_news)
            if amount == len(news_db):
                create_news(news_db)
                return news_db
        url = scrape_next_page_link(response)


get_tech_news(10)
