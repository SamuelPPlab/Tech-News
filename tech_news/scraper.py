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
        return None
    except requests.Timeout:
        return None


# de onde vem os dados
# como fazer as requisições
# como extrair os dados
# como salvar os dados


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    categories_list = selector.css("#js-categories a::text").getall()
    new_categories = []
    sources_list = selector.css(".z--mb-16 div a.tec--badge::text").getall()
    new_sources = []
    scrape_news = {}

    def strip_function(list, new_list):
        for list_item in list:
            new_list.append(list_item.strip())

    strip_function(list=categories_list, new_list=new_categories)
    strip_function(list=sources_list, new_list=new_sources)

    scrape_news["url"] = selector.xpath(
        "//html//head//meta[5]//@content"
    ).get()
    scrape_news["title"] = selector.css(
        ".tec--article__header__title::text"
    ).get()
    scrape_news["writer"] = (
        selector.css(".tec--author__info__link::text").get().strip()
    )
    scrape_news["shares_count"] = int(
        selector.css(".tec--toolbar div::text").get().split()[0]
    )
    scrape_news["timestamp"] = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    scrape_news["comments_count"] = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )
    scrape_news["summary"] = "".join(
        selector.css(".tec--article__body p:first-child *::text").getall()
    )
    scrape_news["sources"] = new_sources
    scrape_news["categories"] = new_categories

    return scrape_news


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)

    return selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()  # @rafaelmguimaraes


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)

    return selector.css(".tec--list--lg a.tec--btn--primary::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
