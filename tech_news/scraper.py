from parsel import Selector
import requests
from time import sleep

# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        sleep(1)
        if (response.status_code != 200):
            raise Exception('Error during request')
        return response.text
    except:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css('.tec--article__header__title').get()
    timestamp = selector.css('.tec--timestamp--lg time::attr(datetime)').get()
    writer = selector.css('.tec--author__info__link::text').get()
    shares_count = selector.css('.tec--toolbar__item::text').get()
    comments_count = selector.css('.tec--toolbar__item button::attr(data-count)').get()
    summary = selector.css('.tec--article__body p:first-of-type *::text').getall()
    sources = selector.css('.z--mb-16 .tec--badge::text').getall()
    categories = selector.css('#js-categories .tec--badge::text').getall()

    return {
        'url': url,
        'title': title[62:len(title) - 5],
        'timestamp': timestamp,
        'writer': writer.strip(),
        'shares_count': int(shares_count.strip().split(' ')[0]),
        'comments_count': int(comments_count),
        'summary': ''.join(summary),
        'sources': [source.strip() for source in sources],
        'categories': [category.strip() for category in categories],
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
