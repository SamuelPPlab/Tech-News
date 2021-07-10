import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)

    except requests.ReadTimeout:
        return None

    return response.text if response.status_code == 200 else None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    data = {}
    data["url"] = selector.css("head link[rel=canonical]::attr(href)").get()
    data["title"] = selector.css("#js-article-title::text").get()
    data["timestamp"] = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get()
    data["writer"] = writer.strip() if writer else None
    shares_count = selector.css(".tec--toolbar__item::text").get()
    data["shares_count"] = int(shares_count.split()[0]) if shares_count else 0
    comments_count = selector.css("#js-comments-btn::text").re_first(r"\d+")
    data["comments_count"] = int(comments_count) if comments_count else 0
    data["summary"] = "".join(
        selector.css(".tec--article__body p:nth-child(1) *::text").getall()
    )
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    data["sources"] = [source.strip() for source in sources]
    categories = selector.css("#js-categories > a *::text").getall()
    data["categories"] = [category.strip() for category in categories]
    return data


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(".tec--card__info h3 a::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(".tec--list a.tec--btn::attr(href)").get()
    return next_page_link


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    response = fetch(url)
    next_page_link = scrape_next_page_link(response)
    news_urls = scrape_novidades(response)
    news = []
    while len(news_urls) < amount:
        response = fetch(next_page_link)
        next_page_link = scrape_next_page_link(response)
        news_urls += scrape_novidades(response)
    for index in range(0, amount):
        new_response = fetch(news_urls[index])
        new_info = scrape_noticia(new_response)
        news.append(new_info)
        print(new_info["title"])
    print('Size', len(news_urls))
    create_news(news)
    return news
