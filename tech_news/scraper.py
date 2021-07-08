import requests
import time
from tech_news.database import create_news
from requests.exceptions import ReadTimeout
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        site = requests.get(url, timeout=3)
        time.sleep(1)
        if site.status_code == 200:
            return site.text
    except ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    sel = Selector(html_content)
    writer = sel.css(".tec--author__info__link::text").get()
    categories = sel.css("#js-categories .tec--badge::text").getall()
    sources = sel.css(".z--mb-16 .tec--badge::text").getall()
    shares = sel.css(".tec--toolbar__item::text").re_first(
        r"\d+"
    )
    comments = sel.css("#js-comments-btn::attr(data-count)").get()
    return {
        "url": sel.css("meta[property='og:url']::attr(content)").get(),
        "title": sel.css(".tec--article__header__title::text").get(),
        "timestamp": sel.css("#js-article-date::attr(datetime)").get(),
        "writer": writer.strip() if writer else None,
        "shares_count": int(shares) if shares else 0,
        "comments_count": int(comments) if comments else 0,
        "summary": "".join(
            sel.css(".tec--article__body > p:first-child *::text").getall()
        ),
        "sources": [source.strip() for source in sources],
        "categories": [categorie.strip() for categorie in categories],
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    return selector.css(
        ".tec--list .tec--card__title__link::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    return selector.css(".tec--btn--primary::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    all_news = []
    url = "https://www.tecmundo.com.br/novidades"
    while len(all_news) < amount:
        html = fetch(url)
        news = scrape_novidades(html)
        all_news.extend([scrape_noticia(fetch(new)) for new in news])
        url = scrape_next_page_link(html)
    all_news = all_news[0:amount]
    create_news(all_news)
    return all_news
