import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        time.sleep(1)
    except (
        requests.ReadTimeout,
        requests.exceptions.RequestException,
        requests.exceptions.HTTPError,
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout
    ):
        return None
    else:
        return response.text


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    writer = selector.css(".tec--author__info__link::text").get()
    shares_count = selector.css(".tec--toolbar__item::text").get()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    news = {}
    news["url"] = selector.css("head link[rel=canonical]::attr(href)").get()
    news["title"] = selector.css(
        "#js-article-title::text").get()
    news["timestamp"] = selector.css("#js-article-date::attr(datetime)").get()
    news["writer"] = writer.strip() if writer is not None else None
    news["shares_count"] = int(
        shares_count[: -len("Compartilharam")].strip()
        if shares_count is not None
        else 0
    )
    news["comments_count"] = int(
        comments_count
        if comments_count is not None
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
    return selector.css("h3 a::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(".tec--btn--lg::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    URL = "https://www.tecmundo.com.br/novidades"
    newsList = list()

    while len(newsList) <= amount:
        page = fetch(URL)
        for item_url in scrape_novidades(page):
            item_text = fetch(item_url)
            news = scrape_noticia(item_text)
            newsList.append(news)
            if len(newsList) == amount:
                create_news(newsList)
                return newsList
            URL = scrape_next_page_link(page)
