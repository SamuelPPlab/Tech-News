import re
import time
import requests

from parsel import Selector
from tech_news.database import create_news

SUCCESS = 200


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=2)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if response.status_code == SUCCESS:
        return response.text


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    shares_count = selector.css(".tec--toolbar__item::text").get()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    summary = selector.css(
        "div.tec--article__body > p:first-child ::text"
    ).getall()
    sources = selector.css("div.z--mb-16.z--px-16 .tec--badge::text").getall()
    categories = selector.css(
        "div.z--px-16 .tec--badge.tec--badge--primary::text"
    ).getall()
    writer = selector.css(".tec--author__info__link::text").get()

    return {
        "url": selector.css("head link[rel=canonical]::attr(href)").get(),
        "title": selector.css("#js-article-title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": writer.strip(),
        "shares_count": int(re.sub(r"\D", "", shares_count)),
        "comments_count": int(comments_count),
        "summary": "".join(summary),
        "sources": [source.strip() for source in sources],
        "categories": [categorie.strip() for categorie in categories],
        }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    try:
        return selector.css("h3 a::attr(href)").getall()
    except Exception:
        return list()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(".tec--btn--lg::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    all_news = list()

    while len(all_news) <= amount :
        request_text = fetch(url)
        for item_url in scrape_novidades(request_text):
            item_text = fetch(item_url)
            news = scrape_noticia(item_text)
            all_news.append(news)
            # if len(all_news) == amount :
        url = scrape_next_page_link(request_text)
    
    return create_news(all_news)


# Referências:

# https://www.w3schools.com/python/python_try_except.asp
# https://stackoverflow.com/questions/24801548/how-to-use-css-selectors-to-retrieve-specific-links-lying-in-some-class-using-be
# https://www.w3schools.com/cssref/sel_firstchild.asp
# https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
# https://docs.python.org/3/library/stdtypes.html#str.strip
# https://www.w3schools.com/python/ref_string_join.asp
