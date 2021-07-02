import requests
import time
from parsel import Selector
from tech_news.database import create_news
from math import ceil


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)

    url = selector.css("meta[property='og:url']::attr(content)").get()

    title = selector.css("#js-article-title::text").get()

    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    writer = selector.css(".tec--author__info__link::text").get()
    if writer:
        writer = writer.strip()

    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count:
        shares_count = int((shares_count.strip()).split(" ")[0])
    else:
        shares_count = 0

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments_count:
        comments_count = int(comments_count)
    else:
        comments_count = 0

    summary = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )

    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    sources = [source.strip() for source in sources]

    categories = selector.css("#js-categories a::text").getall()
    categories = [category.strip() for category in categories]

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(".tec--list__item h3 > a::attr(href)").getall() or []


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(".tec--list > a::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = "https://www.tecmundo.com.br/novidades"
    content = fetch(url)
    news_links = scrape_novidades(content)
    news = []

    for link in news_links:
        link_content = fetch(link)
        new = scrape_noticia(link_content)
        news.append(new)

    pages = ceil(amount / len(news_links))
    if pages > 1:
        for _ in range(1, pages):
            content = fetch(url)
            url = scrape_next_page_link(content)
            content = fetch(url)
            news_links = scrape_novidades(content)
            for link in news_links:
                link_content = fetch(link)
                new = scrape_noticia(link_content)
                news.append(new)
    create_news(news[:amount])
    return news[:amount]
