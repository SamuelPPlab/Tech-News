import requests
import time
from tech_news.database import create_news
from requests.exceptions import ReadTimeout
from parsel import Selector

# Requisito 1
def fetch(url):
    
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
    except ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    
    selector = Selector(html_content)
    writer = selector.css(".tec--author__info__link::text").get()
    categories = selector.css("#js-categories .tec--badge::text").getall()
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    shares = selector.css(".tec--toolbar__item::text").re_first()
    comments = selector.css("#js-comments-btn::attr(data-count)").get()
    return {
        "url": selector.css("meta[property='og:url']::attr(content)").get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": writer.strip() if writer else None,
        "shares_count": int(shares) if shares else 0,
        "comments_count": int(comments) if comments else 0,
        "summary": "".join(selector.css(".tec--article__body > p:first-child *::text").getall()),
        "sources": [source.strip() for source in sources],
        "categories": [categorie.strip() for categorie in categories],
    }


# Requisito 3
def scrape_novidades(html_content):
    
    response = Selector(html_content)
    urlLists = response.css("h3 .tec--card__title__link::attr(href)").getall()
    if urlLists is not None:
        return urlLists
    return []


# Requisito 4
def scrape_next_page_link(html_content):

    response = Selector(html_content)
    nextPageUrl = response.css(
        "a:contains(' Mostrar mais notícias ')::attr(href)"
    ).get()

    return nextPageUrl if nextPageUrl else None

# Requisito 5
def get_tech_news(amount):

    url = "https://www.tecmundo.com.br/novidades"
    links = []

    while len(links) < amount:
        content = fetch(url)
        links += scrape_novidades(content)
        url = scrape_next_page_link(content)

    news_list = []
    for url in links[:amount]:
        content = fetch(url)
        news_list.append(scrape_noticia(content))

    create_news(news_list)
    return news_list
    