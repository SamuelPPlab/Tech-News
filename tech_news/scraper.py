import requests
import time
from parsel import Selector


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news = {}

    news["url"] = selector.css('meta[property="og:url"]::attr(content)').get()

    news["title"] = selector.css(
        'meta[property="og:title"]::attr(content)').get()

    news["timestamp"] = selector.css('time::attr(datetime)').get()

    writer = selector.css('.tec--author__info__link::text').get()
    if writer:
        news["writer"] = writer.strip()
    else:
        news["writer"] = None

    shares_count = selector.css('.tec--toolbar__item::text').get()
    if shares_count:
        news["shares_count"] = int((shares_count.strip()).split(" ")[0])
    else:
        news["shares_count"] = 0

    news["comments_count"] = int(
        selector.css('#js-comments-btn::attr(data-count)').get())

    news["summary"] = "".join(
        selector.css('.tec--article__body > p:first-child *::text').getall())

    news["sources"] = [source.strip() for source in selector.css(
        '.z--mb-16 div a.tec--badge::text').getall()]

    news["categories"] = [categorie.strip() for categorie in selector.css(
        '#js-categories .tec--badge::text').getall()]

    print(news)
    return news


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
