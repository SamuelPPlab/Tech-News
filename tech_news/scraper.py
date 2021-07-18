import requests
import time
from parsel import Selector
# # Requisito 1


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        status = response.status_code
        if status == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None

# Requisito 2 Isabela Cardoso me ajudou com esse requisito


def scrape_noticia(html_content):
    scrape = {}

    def strip_function(list, new_list):
        for list_item in list:
            new_list.append(list_item.strip())

    selector = Selector(html_content)

    scrape["title"] = selector.css(
        ".tec--article__header__title::text"
    ).get()
    scrape["timestamp"] = selector.css(
        "#js-article-date::attr(datetime)"
    ).get()
    scrape["writer"] = selector.css(
        ".tec--author__info__link::text"
    ).get().strip()
    scrape["url"] = selector.xpath("//html//head//meta[5]//@content").get()
    scrape["shares_count"] = int(selector.css(
        ".tec--toolbar__item::text"
    ).get().split()[0])
    scrape["comments_count"] = int(selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get())
    scrape["summary"] = ''.join(selector.css(
        ".tec--article__body p:first-child *::text"
    ).getall())
    sources = selector.css(".z--mb-16 div a.tec--badge::text").getall()
    categories = selector.css("#js-categories a.tec--badge::text").getall()
    source_list = []
    categories_list = []
    strip_function(sources, source_list)
    strip_function(categories, categories_list)
    scrape["sources"] = source_list
    scrape["categories"] = categories_list
    return scrape


# Requisito 3
def scrape_novidades(html_content):
    list_link = []
    selector = Selector(html_content)
    for h3 in selector.css("h3.tec--card__title"):
        link = h3.css("a.tec--card__title__link::attr(href)").get()
        list_link.append(link)
    return list_link


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    mostrar_mais = selector.css(
        "div.tec--list a.tec--btn--lg::attr(href)"
    ).get()
    return mostrar_mais


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
