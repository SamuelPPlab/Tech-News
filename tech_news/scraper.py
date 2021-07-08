import requests
import time
from parsel import Selector

# Requisito 1


def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            time.sleep(1)
            return response.text
        else:
            time.sleep(1)
            return None
    except requests.ReadTimeout:
        time.sleep(1)
        return None


# Requisito 2
def normalize(str_array):
    normalized = []
    for text in str_array:
        normalized.append(text.strip())
    return normalized


def normalize_summary(summary):
    full = ''
    for text in summary:
        full += text
    return full


def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url1 = "https://www.tecmundo.com.br/dispositivos-moveis"
    url2 = "/215327-pixel-5a-tera-lancamento"
    url3 = "-limitado-devido-escassez-chips.htm"
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get()
    shares_count = selector.css(".tec--toolbar__item::text").get()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    summary = selector.css(".tec--article__body *::text").getall()
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories a::text").getall()
    result = {'title': title,
              'timestamp': timestamp,
              'writer': writer.strip(),
              'shares_count': int(shares_count.strip()[0]),
              'comments_count': int(comments_count),
              'summary': normalize_summary(summary[0:7]),
              'sources': normalize(sources),
              'categories': normalize(categories),
              'url': url1 + url2 + url3}
    return result


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news_list = selector.css('.tec--card__thumb + \
    .tec--card__thumb__link::attr(href)').getall()
    print(news_list)
    return news_list


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
