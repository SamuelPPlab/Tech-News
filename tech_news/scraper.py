import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    data = {}
    data["url"] = selector.css("meta[property='og:url']::attr(content)").get()
    data["title"] = selector.css("h1.tec--article__header__title::text").get()
    data["timestamp"] = selector.css("time::attr(datetime)").get()
    data["writer"] = (
        selector.css("a.tec--author__info__link::text").get().strip()
    )

    shares = selector.css("div.tec--toolbar__item::text").get()
    if shares:
        shares_count = int(shares.split()[0])
    else:
        shares_count = 0
    data["shares_count"] = shares_count

    comments = selector.css("button.tec--btn::attr(data-count)").get()
    data["comments_count"] = int(comments)

    summary = selector.css(
        ".tec--article__body p:first-child *::text"
    ).getall()
    data["summary"] = "".join(summary)

    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    data["sources"] = [source.strip() for source in sources]
    categories = selector.css("#js-categories .tec--badge::text").getall()
    data["categories"] = [category.strip() for category in categories]

    return data


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    urls_list = selector.css(
        ".tec--list__item .tec--card__thumb__link::attr(href)"
    ).getall()

    return urls_list


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(".tec--list .tec--btn::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
