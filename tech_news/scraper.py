import requests
import time
from requests.exceptions import ReadTimeout
from parsel import Selector
from tech_news.database import create_news

url = "https://www.tecmundo.com.br/novidades"


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
    except ReadTimeout:
        None


# Requisito 2
# aprendi estudando o codeReview thayscosta3 pull request 92
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    noticia = {}
    selector = Selector(html_content)
    noticia["url"] = selector.css(
        "meta[property='og:url']::attr(content)"
    ).get()
    noticia["title"] = selector.css("#js-article-title::text").get()
    noticia["timestamp"] = selector.css("time::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get()
    writer = writer.strip() if writer else None
    noticia["writer"] = None if not writer else writer
    shares_count = selector.css(".tec--toolbar__item::text").get()
    shares_count = int(shares_count.split()[0]) if shares_count else None
    noticia["shares_count"] = 0 if not shares_count else shares_count

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()

    noticia["comments_count"] = int(comments_count) if comments_count else None
    first_paragraph = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()

    noticia["summary"] = "".join(first_paragraph)
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    noticia["sources"] = [source.strip() for source in sources]

    categories = selector.css("#js-categories .tec--badge::text").getall()
    noticia["categories"] = [category.strip() for category in categories]
    return noticia


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    URL_list = selector.css(
        "h3 > .tec--card__title__link::attr(href)"
    ).getall()
    return URL_list


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    next_page_url = selector.css(".tec--btn::attr(href)").get()
    return next_page_url


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = "https://www.tecmundo.com.br/novidades"
    all_noticia = []

    while len(all_noticia) <= amount:
        request_text = fetch(url)
        for item_url in scrape_novidades(request_text):
            item_text = fetch(item_url)
            news = scrape_noticia(item_text)
            all_noticia.append(news)
            if len(all_noticia) == amount:
                create_news(all_noticia)
                return all_noticia
            url = scrape_next_page_link(request_text)
