import requests
import time
from parsel import Selector
from tech_news.database import create_news

# Requisito 1


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    sources = []
    categories = []
    selector = Selector(text=html_content)

    title = selector.css(".tec--article__header__title::text").get()

    url = selector.css("head > link[rel=canonical]::attr(href)").get()

    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()

    writer = selector.css(".tec--author__info__link::text").get()

    shares_count = selector.css(".tec--toolbar__item::text").get()

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()

    writer, shares_count, comments_count = set_fields(
        writer, shares_count, comments_count
    )

    summary = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )

    for item in selector.css(".z--mb-16 .tec--badge::text").getall():
        sources.append(item.strip())

    for item in selector.css(".tec--badge--primary::text").getall():
        categories.append(item.strip())

    return {
        "title": title,
        "url": url,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


def set_fields(writer, shares_count, comments_count):
    if writer:
        writer = writer.strip()
    if shares_count:
        shares_count = int(shares_count.split("Compartilharam")[0])
    else:
        shares_count = 0
    if comments_count:
        comments_count = int(comments_count)
    return writer, shares_count, comments_count


# Requisito 3
def scrape_novidades(html_content):
    list_news = []
    selector = Selector(text=html_content)
    for item in selector.css(
        ".tec--list--lg .tec--card__title__link::attr(href)"
    ).getall():
        list_news.append(item)
    return list_news


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_button = selector.css(".tec--btn--primary::attr(href)").get()
    return next_button


# Requisito 5
def get_tech_news(amount):
    number_page = 1
    list_news_data = []
    counter = 0

    while amount > counter:
        if number_page == 1:
            url = "https://www.tecmundo.com.br/novidades"
        else:
            url = "https://www.tecmundo.com.br/novidades?page=" + str(
                number_page
            )
        resp_fetch = fetch(url)
        list_news = scrape_novidades(resp_fetch)

        for item in list_news:
            if amount > counter:
                resp_fecth_one_news = fetch(item)
                content_one_news = scrape_noticia(resp_fecth_one_news)
                list_news_data.append(content_one_news)
                counter += 1
        number_page += 1
    create_news(list_news_data)
    return list_news_data
