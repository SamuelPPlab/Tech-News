import requests
import time
from parsel import Selector


# src=https://docs.python-requests.org/en/master/user/quickstart/

# Requisito 1


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        response.raise_for_status()
    except Exception:
        return None
    else:
        return response.text


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    get_url = selector.css("head link[rel=canonical]::attr(href)").get()
    get_title = selector.css("#js-article-title::text").get()
    get_timestamp = selector.css("#js-article-date::attr(datetime)").get()
    get_writer = selector.css(".tec--author__info__link::text").get()
    writer = get_writer.strip()
    get_shares_count = selector.css(
        "#js-author-bar > nav > div:nth-child(1)::text"
    ).get()
    suffix = " Compartilharam"
    get_shares_count = get_shares_count[:-len(suffix)]
    shares_count = int(get_shares_count) if get_shares_count else 0
    get_comments_count = selector.css(
        "#js-comments-btn::attr(data-count)").get()
    comments_count = int(get_comments_count)
    get_summary = selector.css(
        ".tec--article__body p:nth-child(1) *::text"
    ).getall()
    summary = "".join(get_summary)
    get_sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    sources = [source.strip() for source in get_sources]
    get_categories = selector.css("#js-categories  a::text").getall()
    categories = [category.strip() for category in get_categories]
    dic_result = {
        "url": get_url,
        "title": get_title,
        "timestamp": get_timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories
    }
    return dic_result


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    url_list = selector.css(
        "div.tec--card__info h3 a::attr(href)"
    ).getall()
    return url_list


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_link = selector.css("a.tec--btn.tec--btn--lg::attr(href)").get()
    return next_link


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
