from tech_news.database import create_news
import requests
from time import sleep
import re
from parsel import Selector
summary_tag = '.tec--article__body > p:first-child *::text'
shared_tag = '.tec--toolbar__item::text'
sources_tag = 'div.z--mb-16 > div > .tec--badge::text'


# referência:
# https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
def cleaner(html):
    regex = re.compile('<.*?>')
    return re.sub(regex, '', html)


# Requisito 1
def fetch(url):
    try:
        sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None
    return response.text


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css('.tec--article__header__title::text').get()
    writer = selector.css('.tec--author__info__link::text').get()
    shared_count = selector.css(shared_tag).get()
    if isinstance(shared_count, str):
        shared_count = shared_count.strip().split(' ')[0]
    else:
        shared_count = 0
    comments_count = selector.css('#js-comments-btn::attr(data-count)').get()
    if isinstance(comments_count, str):
        comments_count = int(comments_count)
    else:
        comments_count = 0
    summary = selector.css(summary_tag).getall()
    summary = ''.join(summary)
    timestamp = selector.css('#js-article-date::attr(datetime)').get()
    categories = selector.css('#js-categories > .tec--badge::text').getall()
    sources = selector.css(sources_tag).getall()
    sources = list(map(lambda x: x.strip(), sources))
    categories = list(map(lambda x: x.strip(), categories))
    if isinstance(writer, str):
        writer = writer.strip()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shared_count),
        "comments_count": int(comments_count),
        "summary": cleaner(summary),
        "sources": sources,
        "categories": categories
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    tag = '.tec--list__item .tec--card__title > a::attr(href)'
    selector = Selector(html_content)
    list = selector.css(tag).getall()
    return list


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    tag = '.tec--btn.tec--btn--lg.tec--btn--primary.z--mx-auto.z--mt-48'
    attr = '::attr(href)'
    selector = Selector(html_content)
    return selector.css(tag + attr).get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    list = []
    news = 'https://www.tecmundo.com.br/novidades'
    html_content = fetch(news)
    while len(list) + 1 < amount:
        c = amount if amount < 21 else 20
        if amount - len(list) < 21:
            c = amount - len(list)
        links = scrape_novidades(html_content)
        for n in range(c):
            content = fetch(links[n])
            details = scrape_noticia(content)
            list.append(details)
        if (len(list) >= amount):
            break
        news = scrape_next_page_link(fetch(news))
        html_content = fetch(news)
    create_news(list)
    return list
