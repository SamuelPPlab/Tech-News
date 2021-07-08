import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


def count_shares(share_text):
    if share_text is None:
        return int(0)
    share_text = share_text.strip()
    share_quantity = share_text.split(' ')
    if share_text:
        return int(share_quantity[0])
    return int(0)


def remove_space(word):
    if word is None:
        return None
    return word.strip()


# Requisito 2
# https://www.geeksforgeeks.org/python-map-function/
# https://docs.python.org/3/tutorial/datastructures.html
# https://stackoverflow.com/questions/38009787/how-to-extract-meta-description-from-urls-using-python
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    page_content = Selector(html_content)
    news = {}
    news["title"] = page_content.css("#js-article-title::text").get()
    news["writer"] = remove_space(page_content.css(
        ".tec--author__info__link::text").get())
    news["timestamp"] = page_content.css("time::attr(datetime)").get()
    news["shares_count"] = count_shares(page_content.css(
        ".tec--toolbar__item::text").get())
    news["comments_count"] = count_shares(page_content.css(
        "#js-comments-btn::attr(data-count)").get())
    news["summary"] = "".join(page_content.css(
        '.tec--article__body > p:first-child *::text').getall())
    news["sources"] = list(map(remove_space, page_content.css(
        ".z--mb-16 .tec--badge::text").getall()))
    news["categories"] = list(map(remove_space, page_content.css(
        ".tec--badge--primary::text").getall()))
    news["url"] = page_content.css(
        'meta[property="og:url"]::attr(content)').get()
    return news


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    page_content = Selector(html_content)
    news_list = page_content.css(
        "h3 .tec--card__title__link::attr(href)").getall()
    return news_list


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    page_content = Selector(html_content)
    link_to_next = page_content.css(
        '.z--mt-48::attr(href)').get()
    return link_to_next


# Requisito 5
# https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    pages_to_index = -(-amount//20)
    url = 'https://www.tecmundo.com.br/novidades'
    all_news = []
    for _ in range(pages_to_index):
        news = scrape_novidades(fetch(url))
        all_news.extend(news)
        url = scrape_next_page_link(fetch(url))
    news_urls = all_news[0:amount]
    html_of_news = list(map(fetch, news_urls))
    news_content = list(map(scrape_noticia, html_of_news))
    create_news(news_content)
    return news_content
