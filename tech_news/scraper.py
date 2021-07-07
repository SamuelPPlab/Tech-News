import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            response = None
            return response
        return response.text
    except requests.ReadTimeout:
        response = None
        return response


def query_strip(selectorCSS, query):
    if selectorCSS.css(query):
        return selectorCSS.css(
            query
        ).get().strip()
    else:
        return None


# Requisito 2
def scrape_noticia(html_content):
    result = {}
    selector = Selector(text=html_content)
    result["url"] = selector.css("link[rel=canonical]::attr(href)").get()
    result["title"] = query_strip(selector, "h1#js-article-title::text")
    result["timestamp"] = selector.css(
        "time#js-article-date::attr(datetime)"
    ).get()
    result["writer"] = query_strip(selector, "a.tec--author__info__link::text")
    if selector.css("div.tec--toolbar__item::text"):
        result["shares_count"] = int(selector.css(
            "div.tec--toolbar__item::text"
        ).get().strip()[0])
    else:
        result["shares_count"] = 0
    if selector.css("button#js-comments-btn::text"):
        result["comments_count"] = int(selector.css(
            "button#js-comments-btn::attr(data-count)"
        ).get())
    else:
        result["comments_count"] = 0
    result["summary"] = "".join(selector.css(
        "div.tec--article__body > p:first-child *::text"
        ).getall())
    result["sources"] = []
    for source in selector.css("div.z--mb-16 a.tec--badge::text").getall():
        result["sources"].append(source.strip())
    result["categories"] = []
    for category in selector.css("div#js-categories a::text").getall():
        result["categories"].append(category.strip())
    return result


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    list = []
    if selector.css("h3 a.tec--card__title__link"):
        list = selector.css("h3 a.tec--card__title__link::attr(href)").getall()
    else:
        list = []
    return list


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    result = None
    if selector.css("a.z--mx-auto"):
        result = selector.css("a.z--mx-auto::attr(href)").get()
        return result
    else:
        return result


# Requisito 5
def get_tech_news(amount):
    news = []
    page = "https://www.tecmundo.com.br/novidades"
    response = fetch(page)
    newsArray = scrape_novidades(response)
    while len(news) < amount:
        for link in newsArray:
            if len(news) < amount:
                news.append(scrape_noticia(fetch(link)))
            else:
                break

        if len(news) < amount:
            page = scrape_next_page_link(response)
            response = fetch(page)
            newsArray = scrape_novidades(response)
        else:
            break
    create_news(news)
    return news
