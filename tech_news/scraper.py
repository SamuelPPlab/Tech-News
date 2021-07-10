import requests
import time
from parsel import Selector
# from math import ceil
from tech_news.database import create_news


# Requisito 1
def fetch(url):
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
    scrape_info = {}

    selector = Selector(html_content)

    scrape_info['url'] = selector.css(
        "head link[rel=canonical]::attr(href)"
    ).get()

    scrape_info['title'] = selector.css(
        ".tec--article__header__title::text"
    ).get()

    scrape_info['timestamp'] = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()

    scrape_info['writer'] = (
        selector.css(".tec--author__info__link::text").get().strip()
        if selector.css(".tec--author__info__link::text").get() else None
    )

    share_counts_text = selector.css(".tec--toolbar__item::text").get()
    if share_counts_text is not None:
        share_counts = int(share_counts_text.strip().split(' ')[0])
    else:
        share_counts = 0
    scrape_info['shares_count'] = share_counts

    comments_count = selector.css(
        "button#js-comments-btn::attr(data-count)"
    ).get()
    if comments_count is not None:
        scrape_info['comments_count'] = int(comments_count)
    else:
        scrape_info['comments_count'] = 0

    scrape_info['summary'] = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )

    scrape_info['sources'] = [
        font.strip() for font in selector.css(
            "h2:contains('Fontes') + div a::text"
        ).getall()
    ]

    scrape_info['categories'] = [
        category.strip() for category in selector.css(
            "div#js-categories a::text"
        ).getall()
    ]

    return scrape_info


# Requisito 3
def scrape_novidades(html_content):
    response = Selector(html_content)
    urlLists = response.css("h3 .tec--card__title__link::attr(href)").getall()
    if urlLists is not None:
        return urlLists
    return []


# Requisito 4
def scrape_next_page_link(html_content):
    response = Selector(html_content)
    nextPageUrl = response.css(
        "a:contains(' Mostrar mais notícias ')::attr(href)"
    ).get()

    return nextPageUrl if nextPageUrl else None


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    links = []

    while len(links) < amount:
        content = fetch(url)
        links += scrape_novidades(content)
        url = scrape_next_page_link(content)

    news_list = []
    for url in links[:amount]:
        content = fetch(url)
        news_list.append(scrape_noticia(content))

    create_news(news_list)
    return news_list

    # for x in range(ceil(amount/20)):
    #     pageLinks = scrape_novidades(fetch(page))
    #     if page != []:
    #         links.extend(pageLinks)
    #         page = scrape_next_page_link(fetch(page))
    #     else:
    #         print('empty page error')
    # rawhtml = list(map(fetch, links[: -(len(links)-amount) or None]))
    # content = list(map(scrape_noticia, rawhtml))
    # create_news(content)
    # return content
