import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url)
        time.sleep(1)
        if (response.status_code == 200):
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    notice = {}
    try:
        selector = Selector(text=html_content)

        notice["url"] = selector.css(
            "head > meta[property='og:url']::attr(content)"
        ).get()

        notice["title"] = selector.css('#js-article-title::text').get()

        notice["timestamp"] = selector.css(
            '#js-article-date::attr(datetime)'
        ).get()

        notice["writer"] = (
            selector.css('.tec--author__info__link::text').get().strip()
            if selector.css('.tec--author__info__link::text').get() is not None
            else None
        )

        notice["shares_count"] = (
            selector.css('#js-shared').get().strip()
            if selector.css('#js-shared').get() is not None
            else 0
        )

        notice["comments_count"] = (
            selector.css('#js-comment').get().strip()
            if selector.css('#js-comment').get() is not None
            else 0
        )

        notice["summary"] = "".join(selector.css(
            '.tec--article__body > p:first-child *::text'
        ).getall())

        notice["sources"] = [
            source.strip()
            for source in selector.css(
                '.z--mb-16 div a.tec--badge::text'
            ).getall()
        ]

        notice["categories"] = [
            category.strip()
            for category in selector.css('.tec--badge--primary::text').getall()
        ]

        return notice
    except requests.ReadTimeout:
        return None


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
