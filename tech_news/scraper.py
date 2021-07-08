import requests
import time
from parsel import Selector


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
    share_quantity = share_text.split(' ')
    if share_text:
        return int(share_quantity[0])
    return int(0)


def remove_space(word):
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
        ".tec--toolbar__item::text").get().strip())
    news["comments_count"] = int(page_content.css(
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
        ".tec--card__title .tec--card__title__link::attr(href)").getall()
    return news_list


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
