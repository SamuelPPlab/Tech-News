from parsel import Selector
import requests
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
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
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""

    selector = Selector(text=html_content)
    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    writer = selector.css(".tec--author__info__link::text").get()
    if writer is not None:
        writer = writer.strip()
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    if shares_count is not None:
        shares_count = int((shares_count.strip()).split(" ")[0])
    else:
        shares_count = 0
    comments_count = selector.css("#js-comments-btn::text").re_first(r"\d+")
    if comments_count is not None:
        comments_count = int(comments_count)
    summary = "".join(
        selector.css(
            "div.tec--article__body p:nth-child(1) *::text").getall()
    )
    sources = selector.css("div.z--mb-16 a.tec--badge::text").getall()
    sources = [source.strip() for source in sources]
    categories = selector.css("div#js-categories a::text").getall()
    categories = [categorie.strip() for categorie in categories]
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
    all_links = selector.css(
        ".tec--list__item h3 > a::attr(href)").getall() or []
    return all_links


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page = selector.css(".tec--list > a::attr(href)").get()
    return next_page


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = "https://www.tecmundo.com.br/novidades"
    data = []
    while len(data) < amount:
        html_content = fetch(url)
        news_urls = scrape_novidades(html_content)
        for news_url in news_urls:
            news = scrape_noticia(fetch(news_url))
            data.append(news)
        url = scrape_next_page_link(html_content)
    create_news(data)
    return data
