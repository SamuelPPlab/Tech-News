from parsel import Selector
import requests
import time
import six
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


def get_shares_count_format(get_shares_count):
    formated = get_shares_count
    if isinstance(formated, six.string_types):
        formated = get_shares_count.strip()
    if (formated and formated != ' ' and formated != ''):
        return int(get_shares_count.split()[0])
    return 0


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    get_url = selector.css("head link[rel='canonical']::attr(href)").get()
    get_title = selector.css(".z--container h1::text").get()
    get_timestamp = selector.css(".z--flex time::attr(datetime)").get()
    get_writer = selector.css(".tec--author__info__link::text").get()
    get_writer_formated = get_writer.strip() if get_writer else None
    get_shares_count = selector.css(
        "#js-author-bar nav div:first-child *::text"
    ).get()
    get_comments_count = selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get()
    get_summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    get_summary_format = "".join(get_summary)
    get_sources = selector.css(".z--mb-16 div a::text").getall()
    get_sources_format = [source.strip() for source in get_sources]
    get_categories = selector.css("#js-categories > a *::text").getall()
    get_categories_format = [category.strip() for category in get_categories]
    info = {
        "url": get_url,
        "title": get_title,
        "timestamp": get_timestamp,
        "writer": get_writer_formated,
        "shares_count": get_shares_count_format(get_shares_count),
        "comments_count": int(get_comments_count) if get_comments_count else 0,
        "summary": get_summary_format,
        "sources": get_sources_format,
        "categories": get_categories_format,
    }
    return info


# print(scrape_noticia(fetch("https://www.tecmundo.com.br/ciencia/218958-precisamos-saber-novas-variantes-coronavirus.htm")))


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    list_url = selector.css(
        ".tec--list .tec--card__info h3 a::attr(href)"
    ).getall()
    return list_url


# scrape_novidades(fetch("https://www.tecmundo.com.br/novidades"))


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_url = selector.css(".tec--list .tec--btn::attr(href)").get()
    return next_page_url


# scrape_next_page_link(fetch("https://www.tecmundo.com.br/novidades"))


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    list_news = []

    while len(list_news) < amount:
        html_content = fetch(url)
        list_links = scrape_novidades(html_content)

        for link in list_links:
            content_page_html = fetch(link)
            info_link = scrape_noticia(content_page_html)
            list_news.append(info_link)
            if len(list_news) == amount:
                break
        url = scrape_next_page_link(fetch(url))
    create_news(list_news)
    return list_news


# print(get_tech_news(5))
