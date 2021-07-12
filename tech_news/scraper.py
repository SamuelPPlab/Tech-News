import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except Exception:
        return None


# Requisito 2
def scrape_noticia(html_content):

    result = {}

    content = Selector(html_content)

    result["url"] = content.xpath('//html//head//meta[5]//@content').get()
    result["title"] = content.css(".tec--article__header__title::text").get()
    result["timestamp"] = content.css("#js-article-date::attr(datetime)").get()
    result["writer"] = (
        content.css(".tec--author__info__link::text").get().strip()
        if content.css(".tec--author__info__link::text").get() is not None
        else None
    )
    result["shares_count"] = int(
        content.css(".tec--toolbar__item::text").get().strip()[:-15]
        if content.css(".tec--toolbar__item::text").get() is not None
        else 0
    )
    result["comments_count"] = int(
        content.css("#js-comments-btn::attr(data-count)").get()
        if content.css("#js-comments-btn::attr(data-count)").get() is not None
        else 0
    )
    result["summary"] = "".join(
        content.css(".tec--article__body > p:first-child *::text").getall()
    )
    result["sources"] = list(
        map(str.strip, content.css(".z--mb-16 .tec--badge::text").getall())
    )

    result["categories"] = list(
        map(str.strip, content.css("#js-categories > ::text").getall())
    )
    return result


# Requisito 3
def scrape_novidades(html_content):
    result = Selector(html_content).css("\
        h3 > .tec--card__title__link::attr(href)").getall()
    return result


# Requisito 4
def scrape_next_page_link(html_content):
    result = Selector(html_content).css('.tec--btn::attr(href)').get()
    return result


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    news_content = []
    news_links = []

    while len(news_links) < amount:
        content = fetch(url)
        news_links = news_links + scrape_novidades(content)
        url = scrape_next_page_link(content)
    for item in news_links[:amount]:
        news_content.append(scrape_noticia(fetch(item)))

    create_news(news_content)
    return(news_content)
