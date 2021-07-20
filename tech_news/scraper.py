import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    shares_sufix = "Compartilharam"
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

        notice["shares_count"] = int(
            selector.css(
                '.tec--toolbar__item::text'
            ).get()[: -len(shares_sufix)].strip()
            if selector.css('.tec--toolbar__item::text').get() is not None
            else 0
        )

        notice["comments_count"] = int(
            selector.css('#js-comments-btn::attr(data-count)').get().strip()
            if selector.css(
                '#js-comments-btn::attr(data-count)'
            ).get() is not None
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
    selector = Selector(text=html_content)
    try:
        notice_links = (
            selector.css(
                'h3.tec--card__title a.tec--card__title__link::attr(href)'
            ).getall()
            if selector.css(
                'h3.tec--card__title a.tec--card__title__link::attr(href)'
            ).getall() is not None
            else []
        )
        if (len(notice_links) == 0):
            return []
        return notice_links
    except requests.ReadTimeout:
        return []


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    try:
        next_notice_page = (
            selector.css(
                'a.tec--btn::attr(href)'
            ).get()
            if selector.css(
                'a.tec--btn::attr(href)'
            ).get() is not None
            else None
        )
        return next_notice_page
    except requests.ReadTimeout:
        return None


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    notice_links = []
    url = 'https://www.tecmundo.com.br/novidades'

    while ((len(notice_links) < amount)):
        content = fetch(url)
        notice_links.extend(scrape_novidades(content))
        url = scrape_next_page_link(content)

    count = 0
    notices = []
    print(len(notice_links))
    while (count < amount):
        notice_content = fetch(notice_links[count])
        notices.append(scrape_noticia(notice_content))
        count += 1

    create_news(notices)
    return(notices)
