import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.Timeout:
        return None


# Funções Requisito 2
def get_url(selector):
    # https://github.com/tryber/sd-07-tech-news/pull/86/files - Lucas Nonato
    # tech_news/scraper.py linha 24
    url = selector.css(
        'head link[rel=canonical]::attr(href)'
    ).get()
    return url


def get_title(selector):
    title = selector.css(
        '#js-article-title::text'
    ).get()
    return title


def get_timestamp(selector):
    timestamp = selector.css(
        '#js-article-date::attr(datetime)'
    ).get()
    return timestamp


def get_writer(selector):
    writer = selector.css(
        '#js-author-bar > div > p.z--m-none.z--truncate.z--font-bold > a::text'
    ).get()
    if writer:
        return writer.strip()
    else:
        return None


def get_shares_count(selector):
    shares_count = selector.css(
        '#js-author-bar > nav > div:nth-child(1)::text'
    ).get()
    if shares_count:
        shares_suffix = 'Compartilharam'
        shares_count = shares_count[:-len(shares_suffix)]
        return int(shares_count.strip())
    else:
        return 0


def get_comments_count(selector):
    comments_count = selector.css(
        '#js-comments-btn::attr(data-count)'
    ).get()
    if comments_count:
        return int(comments_count)
    else:
        return 0


def get_summary(selector):
    summary_list = selector.css(
        'div.tec--article__body > p:nth-child(1) *::text'
    ).getall()
    expected_summary = ''
    for summary in summary_list:
        expected_summary += summary
    return expected_summary


def get_sources(selector):
    sources_list = selector.css(
        'div.tec--article__body-grid > div.z--mb-16 > div *::text'
    ).getall()
    expected_sources = []
    for source in sources_list:
        if (source == '') or (source == ' '):
            print(source)
        else:
            expected_sources.append(source.strip())
    return expected_sources


def get_categories(selector):
    categories = selector.css(
        '#js-categories *::text'
    ).getall()
    expected_categories = []
    for category in categories:
        if (category == '') or (category == ' '):
            print(category)
        else:
            expected_categories.append(category.strip())
    return expected_categories


# Requisito 2
def scrape_noticia(html_content):
    # https://www.w3schools.com/python/ref_string_strip.asp
    selector = Selector(html_content)
    data = {}

    data['url'] = get_url(selector)
    data['title'] = get_title(selector)
    data['timestamp'] = get_timestamp(selector)
    data['writer'] = get_writer(selector)
    data['shares_count'] = get_shares_count(selector)
    data['comments_count'] = get_comments_count(selector)
    data['summary'] = get_summary(selector)
    data['sources'] = get_sources(selector)
    data['categories'] = get_categories(selector)

    return data


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links_container = selector.css(
        'div > div > article > div > h3 > a::attr(href)'
    ).getall()

    if links_container:
        return links_container
    else:
        return []


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css(
        'div.z--col.z--w-2-3 > div.tec--list.tec--list--lg > a::attr(href)'
    ).get()

    if next_page_link:
        return next_page_link
    else:
        return None


# Requisito 5
def get_tech_news(amount):
    url = 'https://www.tecmundo.com.br/novidades'
    news_info = []
    while len(news_info) < int(amount):
        html_content = fetch(url)
        news_url_list = scrape_novidades(html_content)

        for news_url in news_url_list:
            page_content = fetch(news_url)
            news_info.append(scrape_noticia(page_content))
            if len(news_info) == int(amount):
                create_news(news_info)
                return news_info

        url = scrape_next_page_link(html_content)
