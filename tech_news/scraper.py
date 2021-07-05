from math import ceil
import requests
import time
from parsel import Selector
from tech_news.database import create_news
import re


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url=url, timeout=3)

        if response.status_code == 200:
            return response.text

        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def get_url(selector):
    try:
        url = selector.css("head link::attr(href)").getall()[20]
    except IndexError:
        url = "Undefined"

    return url


def handle_share_counts(shares_count_text):
    if not shares_count_text:
        shares_count = 0
    else:
        shares_count = ""
        for i in shares_count_text:
            if i.isdigit():
                shares_count += i

    return shares_count


def clean_summary(summary_tags):
    clean = re.compile("<.*?>")
    summary = re.sub(clean, "", summary_tags)
    summary = summary.replace('&amp;', '&')

    return summary


def strip_sources(sources_text):
    sources = []
    for source in sources_text:
        sources.append(source.strip())

    return sources


def strip_categories(categories_text):
    categories = []
    for categorie in categories_text:
        categories.append(categorie.strip())

    return categories


def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)

    url = get_url(selector)

    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    try:
        writer = selector.css(".tec--author__info__link::text").get().strip()
    except AttributeError:
        writer = None
    shares_count_text = selector.css(".tec--toolbar__item::text").get()
    try:
        comments_count = int(selector.css(
            "#js-comments-btn::attr(data-count)"
        ).get())
    except TypeError:
        comments_count = 0
    summary_tags = selector.css(".tec--article__body p").get()
    sources_text = selector.css(".z--mb-16 div a::text").getall()
    categories_text = selector.css("#js-categories a::text").getall()

    shares_count = handle_share_counts(shares_count_text)

    summary = clean_summary(summary_tags)

    sources = strip_sources(sources_text)

    categories = strip_categories(categories_text)

    data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }

    return data


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news_list = selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()

    return news_list


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page = selector.css(".tec--btn::attr(href)").get()

    return next_page


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    pages = ceil(amount / 20)

    url = "https://www.tecmundo.com.br/novidades"
    news_links = []
    for _ in range(pages):
        response = fetch(url=url)
        news_links = news_links + scrape_novidades(response)
        url = scrape_next_page_link(response)

    data_news_details = []
    for i in range(amount):
        response = fetch(url=news_links[i])
        data_news_details.append(scrape_noticia(response))

    create_news(data_news_details)
    return data_news_details
