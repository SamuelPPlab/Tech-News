import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    noticia = {}
    noticia["url"] = selector.css(
        "head link[rel='canonical']::attr(href)"
    ).get()
    noticia["title"] = selector.css(".tec--article__header__title::text").get()
    noticia["timestamp"] = selector.css("time::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get()
    noticia["writer"] = writer.strip()
    shares = selector.css(".tec--toolbar__item::text").get()
    noticia["shares_count"] = int(shares[1:2])
    noticia["comments_count"] = int(
        selector.css(".tec--btn::attr(data-count)").get()
    )
    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    noticia["summary"] = "".join(summary)
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    for i in range(len(sources)):
        sources[i] = sources[i].strip()
    noticia["sources"] = sources
    categories = selector.css("#js-categories > a::text").getall()
    for i in range(len(categories)):
        categories[i] = categories[i].strip()
    noticia["categories"] = categories
    print(noticia)
    return noticia


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    novidades_url = []
    for urls in selector.css(".tec--list.tec--list--lg .tec--list__item"):
        novidades_url.append(urls.css("a::attr(href)").get())
    return novidades_url


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


scrape_novidades(fetch("https://www.tecmundo.com.br/novidades"))
