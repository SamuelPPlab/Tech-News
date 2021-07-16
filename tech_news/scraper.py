import requests
import time
from parsel import Selector
import re


def url_ok(request):
    return request.status_code == 200


# Requisito 1
# Baseado em:
# https://github.com/tryber/sd-07-tech-news/blob/nonato-tech-news/tech_news/scraper.py
def fetch(url):
    try:
        time.sleep(1)
        page = requests.get(url)
        if url_ok(page):
            return page.text
        return None

    except requests.ReadTimeout:
        return None


def extract_num(string):
    return re.findall(r'\d+', string)[0]


def get_writer(page):
    writer = page.css('a[class=tec--author__info__link]::text').get()
    if writer:
        return writer[1:][:-1]
    return None


def get_shares_count(page):
    text = page.css('div[class=tec--toolbar__item]::text').get()
    if text:
        shares_count = int(extract_num(text))
        return shares_count
    return 0


def get_comments_count(page):
    text = int(page.css('#js-comments-btn::attr(data-count)').get())
    return text


def get_summary(page):
    css_to_find = '.tec--article__body > p:first-child *::text'
    paragraph_elems = page.css(css_to_find).getall()
    separator = ''
    formated_paragraph = separator.join(paragraph_elems)
    return formated_paragraph


def get_sources(page):
    sources = page.css('a[target].tec--badge *::text').getall()
    formated_sources = []
    for source in sources:
        if source != ' ':
            formated_sources.append(source[1:][:-1])
    return formated_sources


def get_categories(page):
    categories = page.css('#js-categories *::text').getall()
    formated_categories = []
    for category in categories:
        if category != ' ':
            formated_categories.append(category[1:][:-1])

    return formated_categories


# Requisito 2
def scrape_noticia(html_content):
    page = Selector(html_content)

    result_data = {
        'url': page.css('link[rel^=canonical]::attr(href)').get(),
        'title': page.css('h1::text').get(),
        'timestamp': page.css('time::attr(datetime)').get(),
        'writer': get_writer(page),
        'shares_count': get_shares_count(page),
        'comments_count': get_comments_count(page),
        'summary': get_summary(page),
        'sources': get_sources(page),
        'categories': get_categories(page)
    }
    return result_data


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
