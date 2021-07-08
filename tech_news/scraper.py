import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    time = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get()

    if writer:
        writer = writer.strip()
    else:
        writer = None

    shares_count = selector.css(".tec--toolbar__item::text").get()

    if shares_count:
        shares_count = int((shares_count.strip()).split(" ")[0])
    else:
        shares_count = 0

    comments = selector.css(
        "#js-comments-btn::attr(data-count)").get()

    if comments:
        comments = int(comments)
    else:
        comments = 0

    summary = selector.css(
        ".tec--article__body > p:first-child *::text").getall()
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories a::text").getall()

    return {
      "url": url,
      "title": title,
      "timestamp": time,
      "writer": writer,
      "shares_count": shares_count,
      "comments_count": comments,
      "summary": "".join(summary),
      "sources": [source.strip() for source in sources],
      "categories": [category.strip() for category in categories],
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news_links = selector.css(
        "div.tec--list a.tec--card__thumb__link::attr(href)").getall()
    return news_links


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_link = selector.css(
        ".tec--list .tec--btn::attr(href)").get()
    return next_link


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = "https://www.tecmundo.com.br/novidades"
    scraped_news = []

    while True:
        news_content = fetch(url)
        news_links = scrape_novidades(news_content)
        for news in news_links:
            news_detail = fetch(news)
            scraped_details = scrape_noticia(news_detail)
            scraped_news.append(scraped_details)
            if len(scraped_news) == amount:
                create_news(scraped_news)
                return scraped_news
        url = scrape_next_page_link(news_content)
