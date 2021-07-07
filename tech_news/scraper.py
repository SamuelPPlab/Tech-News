import requests
import time
from parsel import Selector
from tech_news.database import create_news


url = "https://www.tecmundo.com.br/novidades"


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
""" REF função STRIP:
https://pt.stackoverflow.com/questions/107841/fun%C3%A7%C3%A3o-equivalente-ao-trim-fun%C3%A7%C3%A3o-para-remover-espa%C3%A7os-extras-no-in%C3%ADcio-e-fim
"""


def scrape_noticia(html_content):
    page = Selector(html_content)
    news = {}
    news["url"] = page.css("meta[property='og:url']::attr(content)").get()
    news["title"] = (
        page.css(".tec--article__header__title::text").get().strip()
    )
    news["timestamp"] = (
        page.css(".tec--timestamp__item > time::attr(datetime)").get().strip()
    )
    news["writer"] = (
        page.css(".tec--author__info__link::text").get().strip()
        if page.css(".tec--author__info__link::text")
        else None
    )
    news["shares_count"] = (
        int(page.css(".tec--toolbar__item::text").get()[:2])
        if page.css(".tec--toolbar__item::text")
        else 0
    )

    news["comments_count"] = int(
        page.css("#js-comments-btn::attr(data-count)").get()
    )

    news["summary"] = "".join(
        page.css(".tec--article__body > p:first-child *::text").getall()
    )

    news["sources"] = []
    news["categories"] = []

    for new in page.css(".z--mb-16 > div > a::text").getall():
        news["sources"].append(new.strip())

    for categorie in page.css("#js-categories > a::text").getall():
        news["categories"].append(categorie.strip())

    return news


# Requisito 3
def scrape_novidades(html_content):
    page = Selector(text=html_content)
    allLink = page.css("h3 > .tec--card__title__link::attr(href)").getall()
    return allLink


# Requisito 4
def scrape_next_page_link(html_content):
    print(html_content)
    page = Selector(text=html_content)
    nextPage = page.css(".tec--btn::attr(href)").get()
    return nextPage


# Requisito 5
def get_tech_news(amount):
    next_page_url = "https://www.tecmundo.com.br/novidades?page=1"
    allNews = []
    counter = 0

    while next_page_url and counter <= amount:
        response = fetch(next_page_url)
        selector = Selector(text=response)
        allLinks = scrape_novidades(response)
        for link in allLinks:
            counter += 1
            if counter <= amount:
                item = fetch(link)
                scrape_item = scrape_noticia(item)
                allNews.append(scrape_item)

        next_page_url = selector.css(".tec--btn::attr(href)").get()
    create_news(allNews)
    return allNews
