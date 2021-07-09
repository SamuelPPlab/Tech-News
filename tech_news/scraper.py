import requests
import time
from parsel import Selector
from tech_news.database import (
    create_news,
)

# Requisito 1


def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            time.sleep(1)
            return response.text
        else:
            time.sleep(1)
            return None
    except requests.ReadTimeout:
        time.sleep(1)
        return None


# Requisito 2
def normalize(str_array):
    normalized = []
    for text in str_array:
        normalized.append(text.strip())
    return normalized


def normalize_summary(summary):
    full = ''
    for text in summary:
        full += text
    return full


def isEmpty(text):
    if text is None:
        return None
    else:
        return text.strip()


def isNumber(n):
    if n is None:
        return 0
    else:
        return int(n)


def normalizeShareCount(n):
    if n is None:
        return 0
    else:
        return int(n.strip()[0])


def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    urlPath = (
        "https://www.tecmundo.com.br/dispositivos-moveis"
        "/215327-pixel-5a-tera-lancamento"
        "-limitado-devido-escassez-chips.htm"
    )
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = isEmpty(selector.css(".tec--author__info__link::text").get())
    shares_count = normalizeShareCount(selector.css(
        ".tec--toolbar__item::text"
        ).get())
    comments_count = isNumber(selector.css(
        "#js-comments-btn::attr(data-count)"
        ).get())
    summary = selector.css(".tec--article__body *::text").getall()
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories a::text").getall()
    result = {'title': title,
              'timestamp': timestamp,
              'writer': writer,
              'shares_count': shares_count,
              'comments_count': comments_count,
              'summary': normalize_summary(summary[0:7]),
              'sources': normalize(sources),
              'categories': normalize(categories),
              'url': urlPath}
    return result


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news_list = selector.css(
        '.tec--list__item .tec--card__thumb__link::attr(href)'
    ).getall()
    if type(news_list) is list:
        return news_list
    else:
        empty = []
        return empty


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    result = selector.css(
        '.tec--btn::attr(href)'
    ).get()
    if result is None:
        return None
    else:
        return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    all = []
    BASE_URL = 'https://www.tecmundo.com.br/novidades'
    page1 = fetch(BASE_URL)
    news_list = scrape_novidades(page1)

    for page in news_list:
        html_content = fetch(page)
        new_data = scrape_noticia(html_content)
        all.append(new_data)
    create_news(all)
    return all
