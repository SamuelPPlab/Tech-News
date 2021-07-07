from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url)
    except requests.ReadTimeout:
        return None
    else:
        if response.status_code == 200:
            return response.text
        return None


def aaa():
    return "ab"


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css("h1#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css("a.tec--author__info__link::text").get()
    shares_count = selector.css("div.tec--toolbar__item::text").re_first(
        r"\d+"
    )
    comments_count = selector.css("#js-comments-btn::text").re_first(r"\d+")
    summary = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )
    sources = selector.css("div.z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories a.tec--badge::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer.strip() if writer else writer,
        "shares_count": (int(shares_count) if shares_count else shares_count),
        "comments_count": (
            int(comments_count) if comments_count else comments_count
        ),
        "summary": summary,
        "sources": [source.strip() for source in sources]
        if sources
        else sources,
        "categories": [categorie.strip() for categorie in categories]
        if categories
        else categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    # tec--card__title__link
    selector = Selector(text=html_content)
    return selector.css("h3 > a.tec--card__title__link::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# print(
#     scrape_noticia(
#         fetch(
#             "https://www.tecmundo.com.br/minha-serie/220561-wandavision-roteiristas-nao-entenderam-trama-serie-marvel.htm"
#         )
#     )
# )
