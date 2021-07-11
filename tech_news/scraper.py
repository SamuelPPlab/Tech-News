import requests
import time
from parsel import Selector

# Requisito 1


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css("meta[property='og:title']::attr(content)").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get()
    shares_count = selector.css(
        "#js-author-bar > nav > div:nth-child(1)::text"
    ).get()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    summary = "".join(selector.css(
            ".tec--article__body > p:first-child *::text"
        ).getall()),
    sources = list(map(
            str.strip,
            selector.css("div.z--mb-16 .tec--badge::text").getall(),
        )),
    categories = list(map(
            str.strip,
            selector.css("div#js-categories a.tec--badge::text").getall(),
        )),
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer.strip() if writer is not None else None,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
