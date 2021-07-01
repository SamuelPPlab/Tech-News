import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    html = Selector(text=html_content)
    data = {}
    data["url"] = html.css("meta[property='og:url']::attr(content)").get()
    data["title"] = (
        html.css(".tec--article__header__title::text").get().strip()
    )
    data["timestamp"] = html.css("time::attr(datetime)").get().strip()
    data["writer"] = (
        html.css(".tec--author__info__link::text").get().strip()
        if html.css(".tec--author__info__link::text")
        else None
    )
    data["shares_count"] = int(
        html.css(".tec--toolbar__item::text").get().strip()[:2]
    )
    data["comments_count"] = int(
        html.css("#js-comments-btn::attr(data-count)").get()
    )
    data["summary"] = "".join(
        html.css(".tec--article__body > p:first-child *::text").getall()
    )
    data["sources"] = [
        source.strip()[9:]
        for source in html.css(".z--mb-16 a.tec--badge::attr(title)").getall()
    ]
    data["categories"] = [
        categorie.strip()[9:]
        for categorie in html.css(".tec--badge--primary::attr(title)").getall()
    ]
    return data


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    html = Selector(text=html_content)
    return html.css("h3 a.tec--card__title__link::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    return Selector(text=html_content).css(".tec--btn::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
