import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text

        else:
            return None

    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    news = {}
    news["url"] = selector.css("head link[rel=canonical]::attr(href)").get()
    news["title"] = selector.css(".tec--article__header__title::text").get()
    news["timestamp"] = selector.css("time::attr(datetime)").get()
    news["writer"] = selector.css(".tec--author__info__link::text").get()

    if news["writer"]:
        news["writer"] = (
            selector.css(".tec--author__info__link::text").get().strip()
        )
    news["shares_count"] = selector.css(".tec--toolbar__item::text").get()

    if news["shares_count"]:
        news["shares_count"] = int(news["shares_count"].split(" ")[1])
    else:
        news["shares_count"] = 0
    news["comments_count"] = selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get()
    if news["comments_count"]:
        news["comments_count"] = int(news["comments_count"])
    else:
        news["comments_count"] = 0

    news["summary"] = "".join(
        selector.css(".tec--article__body p:first-child *::text").getall()
    )
    news["sources"] = [
        source.strip()
        for source in selector.css(".z--mb-16 .tec--badge::text").getall()
    ]
    news["categories"] = [
        category.strip()
        for category in selector.css(
            "#js-categories .tec--badge::text"
        ).getall()
    ]
    return news


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(
        ".tec--list--lg .tec--list__item .tec--card__title a::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    nextpage = selector.css(".tec--list--lg .tec--btn::attr(href)").get()
    if nextpage:
        return nextpage

    else:
        return None

    # html = fetch("https://www.tecmundo.com.br/novidades")
    # scrape_next_page_link(html)


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
