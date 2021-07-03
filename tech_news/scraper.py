from parsel import Selector
import requests
import time
from tech_news.database import create_news, find_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if response.status_code == 200:
        return response.text
    else:
        return None


def check_exists_int(item, returns, num):
    if item is None:
        return returns
    elif item is not None and num == 1:
        return int(item[1])
    else:
        return int(item)


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    def check_exists_string(item1, item2):
        if selector.css(item1).get() is None:
            return None
        else:
            return selector.css(item1).get().strip()

    info_news = {}
    title = ".tec--article__header__title::text"
    timestamp = "#js-article-date::attr(datetime)"
    author_option_one = ".tec--author__info__link::text"
    author_option_two = ".z--font-bold a::text"
    shared = ".tec--toolbar__item::text"
    coments = "#js-comments-btn::attr(data-count)"
    summary = ".tec--article__body p:first-child *::text"
    source = ".z--mb-16 div a::text"
    categorie = "#js-categories a::text"
    categories = []
    sources = []
    for source in selector.css(source).getall():
        sources.append(source.strip())
    for category in selector.css(categorie).getall():
        categories.append(category.strip())
    info_news["url"] = selector.css(
        "meta[property='og:url']::attr(content)"
    ).get()
    info_news["title"] = selector.css(title).get()
    info_news["timestamp"] = selector.css(timestamp).get()
    info_news["writer"] = check_exists_string(
        author_option_one, author_option_two)
    info_news["shares_count"] = check_exists_int(
        selector.css(shared).get(), 0, 1)
    info_news["comments_count"] = check_exists_int(
        selector.css(coments).get(), 0, 0)
    info_news["summary"] = "".join(selector.css(summary).getall())
    info_news["sources"] = sources
    info_news["categories"] = categories

    return info_news


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news = selector.css(".tec--list--lg h3 a::attr(href)").getall()
    return news


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    url_next = selector.css(".tec--btn--lg::attr(href)").get()
    return url_next


# Requisito 5
def get_tech_news(amount):
    next_url = "https://www.tecmundo.com.br/novidades"
    result = []
    while len(result) <= amount/2:
        response_page = fetch(next_url)
        list_news_pages = scrape_novidades(response_page)
        for url_news in list_news_pages:
            url = fetch(url_news)
            response_url = scrape_noticia(url)
            result.append(response_url)

        next_url = scrape_next_page_link(response_page)
    create_news(result[:amount])
    return find_news()
