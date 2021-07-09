import requests
import time
from parsel import Selector

# import tech_news.database as db


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None

    time.sleep(1)

    if response.ok:
        return response.text
    else:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)

    return {
        "url": selector.css("head > link:nth-child(26)")
        .css("link::attr(href)")
        .get(),
        "title": selector.css("h1::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": selector.css("#js-author-bar div p a::text").get().strip(),
        "shares_count": int(
            selector.css("#js-author-bar nav div::text").get().split()[0]
        ),
        "comments_count": int(
            selector.css(
                "#js-author-bar nav div button::attr(data-count)"
            ).get()
        ),
        "summary": "".join(
            selector.css(".tec--article__body p:nth-child(1) *::text").getall()
        ),
        "sources": [
            source.strip()
            for source in selector.css(".z--mb-16 div a::text").getall()
        ],
        "categories": [
            category.strip()
            for category in selector.css("#js-categories a::text").getall()
        ],
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(
        ".tec--list__item article div h3 a::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(".tec--btn::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    html = fetch("https://www.tecmundo.com.br/novidades")
    urls = scrape_novidades(html)
    html_news = []  # colocar o html de cada link aqui
    i = 0

    while i <= amount:
        for url in urls:
            new = scrape_noticia(fetch(url))
            html_news.append(new)
            if i == 20 or i == 30:
                scrape_next_page_link(html)
            i += 1
