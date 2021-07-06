import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=1)
        response.raise_for_status()
    except Exception:
        return None
    else:
        return response.text


def stripper(word):
    return word.strip()

# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return{
        "url": selector.css("head > [rel=canonical]::attr(href)").get(),
        "title": selector.css("h1.tec--article__header__title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": selector.css("a.tec--author__info__link::text")
        .get().strip(),
        "shares_count": int(selector.css("div.tec--toolbar__item::text").get()
        .split()[0]),
        "comments_count": int(selector.css("button.tec--btn::attr(data-count)")
        .get()),
        "summary": "".join(
            selector.css(".tec--article__body p:first-child *::text").getall()
            ),
        "sources":
        list(map(stripper, selector.css("div.z--mb-16 a.tec--badge::text")
        .getall())),
        "categories": list(map(stripper, selector.css("a.tec--badge--primary::text")
        .getall())),
    }


print(scrape_noticia(fetch('https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm')))


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(".tec--list__item h3 > a::attr(href)").getall() or []


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
