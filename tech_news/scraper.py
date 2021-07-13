import requests
import time
from parsel import Selector
from tech_news.database import create_news
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
    newsletter = {}
    newsletter["url"] = selector.css(
        "head > meta[property='og:url']::attr(content)"
    ).get()
    newsletter["title"] = selector.css("#js-article-title::text").get()
    newsletter["timestamp"] = selector.css(
        "#js-article-date::attr(datetime)"
    ).get()
    newsletter["writer"] = (
        selector.css(".tec--author__info__link::text").get().strip()
        if selector.css(".tec--author__info__link::text").get() is not None
        else None
        # source: github Anderson Alves
    )
    newsletter["shares_count"] = int(
        selector.css(".tec--toolbar__item::text")
        .get()
        .strip()[: -len("Compartilharam")]
        if selector.css(".tec--toolbar__item::text").get() is not None
        else 0
        # source: github Anderson Alves
    )
    newsletter["comments_count"] = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
        if selector.css("#js-comments-btn::attr(data-count)").get() is not None
        else 0
        # source: github Anderson Alves
    )
    newsletter["summary"] = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )
    newsletter["sources"] = list(
        map(
            str.strip,
            selector.css(".z--mb-16 div a.tec--badge::text").getall(),
        )
    )
    newsletter["categories"] = list(
        map(
            str.strip,
            selector.css("#js-categories a.tec--badge::text").getall(),
        )
    )

    return newsletter


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
    response = selector.css(".tec--btn::attr(href)").get()

    return response


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = "https://www.tecmundo.com.br/novidades"
    news = []
    news_list = []
    while len(news_list) < amount:
        response = fetch(url)
        news_list += scrape_novidades(response)
        url = scrape_next_page_link(response)
    for link in news_list[:amount]:
        news.append(scrape_noticia(fetch(link)))

    create_news(news)
    return news


pp = pprint.PrettyPrinter(indent=4)
fetched_data = fetch("https://www.tecmundo.com.br/novidades")
pp.pprint(scrape_next_page_link(fetched_data))
# pp.pprint(scrape_novidades(fetched_data))
