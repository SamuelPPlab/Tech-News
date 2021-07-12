import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)

        if (response.status_code == 200):
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    scrape = {}
    selector = Selector(text=html_content)
    scrape['url'] = selector.css("meta[property='og:url']::attr(content)").get()
    scrape['title'] = selector.css(".tec--article__header__title::text").get()
    scrape['timestamp'] = selector.css("time::attr(datetime)").get()
    scrape['writer'] = selector.css(".tec--author__info__link::text").get()
    if scrape['writer'] is not None:
        scrape['writer'] = scrape['writer'].strip()

    scrape['shares_count'] = selector.css(
        ".tec--toolbar__item::text"
    ).get()

    if scrape['shares_count']:
        scrape['shares_count'] = int(scrape['shares_count'].split(' ')[1])
    else:
        scrape['shares_count'] = 0

    scrape['comments_count'] = selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get()

    if scrape['comments_count']:
        scrape['comments_count'] = int(scrape['comments_count'])
    else:
        scrape['comments_count'] = 0

    scrape['summary'] = "".join(selector.css(
        ".tec--article__body p:first-child *::text"
    ).getall())
    scrape['sources'] = list(map(str.strip, selector.css(
        ".z--mb-16 div a.tec--badge::text"
    ).getall()))
    scrape['categories'] = list(map(str.strip, selector.css(
        "div#js-categories a.tec--badge::text"
    ).getall()))

    return scrape


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
