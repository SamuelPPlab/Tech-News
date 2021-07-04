import requests
import time
from parsel import Selector
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
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css("head link::attr(href)").getall()[20]
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    writer = selector.css(".tec--author__info__link::text").get().strip()
    shares_count_text = selector.css(".tec--toolbar__item::text").get()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    summary_tags = selector.css(".tec--article__body p").get()
    sources_text = selector.css(".z--mb-16 div a::text").getall()
    categories_text = selector.css("#js-categories a::text").getall()

    if not shares_count_text:
        shares_count = 0
    else:
        shares_count = ""
        for i in shares_count_text:
            if i.isdigit():
                shares_count += i

    clean = re.compile("<.*?>")
    summary = re.sub(clean, "", summary_tags)

    sources = []
    for source in sources_text:
        sources.append(source.strip())

    categories = []
    for categorie in categories_text:
        categories.append(categorie.strip())

    data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
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
