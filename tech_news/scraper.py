from parsel import Selector
import requests
from time import sleep

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        sleep(1)
        if (response.status_code != 200):
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css('.tec--article__header__title::text').get()
    timestamp = selector.css('.tec--timestamp--lg time::attr(datetime)').get()
    writer = selector.css('.tec--author__info__link::text').get()
    shares_count = selector.css('.tec--toolbar__item::text').get()
    comments_count = selector.css('#js-comments-btn::attr(data-count)').get()
    summary = selector.css(
        '.tec--article__body > p:first-child *::text'
    ).getall()
    sources = selector.css('.z--mb-16 .tec--badge::text').getall()
    categories = selector.css('#js-categories .tec--badge::text').getall()

    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer.strip() if writer is not None else None,
        'shares_count':
            int(shares_count.strip().split(' ')[0])
            if shares_count is not None else 0,
        'comments_count':
            int(comments_count)
            if comments_count is not None else 0,
        'summary': ''.join(summary),
        'sources': [source.strip() for source in sources],
        'categories': [category.strip() for category in categories],
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css(
        '.tec--list__item .tec--card__title__link::attr(href)'
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css('.tec--list > a::attr(href)').get()


# Requisito 5
def get_tech_news(amount):
    next_url = 'https://www.tecmundo.com.br/novidades'
    news_per_page = 20
    news_to_fetch = amount

    fetched_news = []
    fetched_news_count = 0
    page_number = 1

    while next_url:
        html_content = fetch(next_url)
        news_list = scrape_novidades(html_content)

        for i in range(min(news_to_fetch, news_per_page)):
            content = fetch(news_list[i])
            news = scrape_noticia(content)
            fetched_news.append(news)
            fetched_news_count += 1

        if (amount > (news_per_page * page_number)):
            news_to_fetch -= news_per_page
            page_number += 1

        if (amount == fetched_news_count):
            break

        next_url = scrape_next_page_link(html_content)

    create_news(fetched_news)
    return fetched_news
