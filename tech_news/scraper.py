import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except Exception as error:
        print("Error: ", error)
        return None
    else:
        return response.text


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    newsList = {}
    selector = Selector(html_content)
    newsList["url"] = selector.css(
        "meta[property='og:url']::attr(content)"
    ).get()
    newsList["title"] = selector.css("#js-article-title::text").get()
    newsList["timestamp"] = selector.css(
        "#js-article-date::attr(datetime)"
    ).get()
    newsList["writer"] = (
        selector.css(".tec--author__info__link::text").get().strip()
        if selector.css(".tec--author__info__link::text").get() is not None
        else None
    )
    newsList["shares_count"] = int(
        selector.css(".tec--toolbar__item::text").get()[:-15]
        if selector.css(".tec--toolbar__item::text").get() is not None
        else 0
    )
    newsList["comments_count"] = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
        if selector.css("#js-comments-btn::attr(data-count)").get() is not None
        else 0
    )
    newsList["summary"] = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )
    newsList["sources"] = list(
        map(
            str.strip,
            selector.css('a[rel="noopener nofollow"]::text').getall(),
        )
    )
    newsList["categories"] = list(
        map(str.strip, selector.css("#js-categories > ::text").getall())
    )
    return newsList


# Requisito 3
def scrape_novidades(html_content):
    selector = (
        Selector(html_content)
        .css("h3 > a[class='tec--card__title__link']::attr(href)")
        .getall()
    )
    return selector


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content).css(".tec--btn::attr(href)").get()
    return selector


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    news_titles = []
    titles = []
    while len(news_titles) < amount:
        html_content = fetch(url)
        news_titles = news_titles + scrape_novidades(html_content)
        url = scrape_next_page_link(html_content)
    for link in news_titles[:amount]:
        titles.append(scrape_noticia(fetch(link)))
    return titles


novidades = fetch("https://www.tecmundo.com.br/novidades")
print(len(scrape_novidades(novidades)))
