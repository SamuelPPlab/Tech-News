import requests
import time
from parsel import Selector
from .database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except Exception as e:
        print("Error exception: ", e)
        return None
    else:
        return response.text


# Requisito 2
def scrape_noticia(html_content):
    news_dic = {}
    selector = Selector(html_content)

    news_dic["url"] = selector.css(
        'meta[property="og:url"]::attr(content)'
    ).get()

    news_dic["title"] = selector.css("#js-article-title::text").get()

    news_dic["timestamp"] = selector.css(
        "#js-article-date::attr(datetime)"
    ).get()

    writer = selector.css(".tec--author__info__link::text").get()
    if writer is not None:
        news_dic["writer"] = writer.strip()
    else:
        news_dic["writer"] = None

    news_dic["shares_count"] = int(
        selector.css(".tec--toolbar__item::text")
        .get(default="0")
        .replace("Compartilharam", "")
        .strip()
    )

    news_dic["comments_count"] = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )

    news_dic["summary"] = "".join(
        (selector.css(".tec--article__body > p:first-child *::text").getall())
    )

    news_dic["sources"] = list(
        map(
            str.strip,
            selector.css("div > div > a[class='tec--badge']::text").getall(),
        )
    )

    news_dic["categories"] = [
        item.strip(" ")
        for item in selector.css("#js-categories > a::text").getall()
    ]

    return news_dic


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css("h3 > .tec--card__title__link::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(".tec--btn::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    news_link_list = []

    while len(news_link_list) < amount:
        content = fetch(url)
        news_link_list += scrape_novidades(content)
        url = scrape_next_page_link(content)

    news_list = []
    for url in news_link_list[:amount]:
        content = fetch(url)
        news_list.append(scrape_noticia(content))

    create_news(news_list)
    return news_list
