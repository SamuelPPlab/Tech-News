import requests
from time import sleep
import parsel
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    sleep(1)

    try:
        response = requests.get(url, timeout=3)

        if response.status_code == 200:
            return response.text

        return None

    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    scrape_info = {}

    selector = parsel.Selector(html_content)

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
    selector = parsel.Selector(html_content)

    linkList = selector.css(
        "h3.tec--card__title .tec--card__title__link::attr(href)").getall()

    if (linkList is not None):
        return linkList
    return []


# Requisito 4
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)

    nextPageLink = selector.css(
        "a:contains(' Mostrar mais notícias ')::attr(href)"
    ).get()

    return nextPageLink if nextPageLink else None


# Requisito 5
def get_tech_news(amount):
    allNewsList = []
    linksList = []

    url_path = 'https://www.tecmundo.com.br/novidades'
    while len(linksList) <= amount:
        html_content = fetch(url_path)
        newsList = scrape_novidades(html_content)

        linksList = linksList + newsList

        nextPageUrl = scrape_next_page_link(html_content)

        if nextPageUrl == 'https://www.tecmundo.com.br/novidades?page=3':
            break

        url_path = nextPageUrl

    for index in range(0, amount):
        news_html = fetch(linksList[index])
        news = scrape_noticia(news_html)
        allNewsList.append(news)

    create_news(allNewsList)
    return allNewsList
