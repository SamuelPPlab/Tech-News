import parsel
import pymongo
import requests
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    selector = selector.css(".tec--article")

    start_index = html_content.find("@id")
    end_index = html_content.find("}}", start_index)
    url = html_content[(start_index + 6):(end_index - 1)]

    title = selector.css("#js-article-title::text").get()
    if title:
        title = title.strip()
    else:
        title = None

    timestamp = selector.css("time#js-article-date::attr(datetime)").get()

    writer = selector.css("a.tec--author__info__link::text").get()
    if writer:
        writer = writer.strip()
    else:
        writer = None

    shares_count = selector.css("div.tec--toolbar__item::text").re_first(r"\d")
    if shares_count:
        shares_count = int(shares_count)
    else:
        shares_count = 0

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments_count:
        comments_count = int(comments_count)
    else:
        comments_count = 0

    summary_css = ".tec--article__body > p:nth-child(1) *::text"
    summary = selector.css(summary_css).getall()
    summary = "".join(summary)

    sources = selector.css("div > .tec--badge[target=_blank]::text").getall()
    sources = [source.strip() for source in sources]

    categories = selector.css("#js-categories a::text").getall()
    categories = [category.strip() for category in categories]

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    links = selector.css(
        "div.tec--list.tec--list--lg "
        + "div.tec--list__item "
        + "article.tec--card.tec--card--medium "
        + "figure.tec--card__thumb "
        + "a.tec--card__thumb__link::attr(href)"
    ).getall()

    filtered_links = []
    for link in links:
        if link not in filtered_links:
            filtered_links.append(link)

    return filtered_links


# Requisito 4
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    next_link = selector.css("div.tec--list > a:last-child::attr(href)").get()

    if not next_link:
        return None
    return next_link


# Requisito 5
def get_news_url_list(amount):
    news_page_url = "https://www.tecmundo.com.br/novidades"
    news_url_list = []

    while len(news_url_list) < amount:
        html = fetch(news_page_url)
        url_list = scrape_novidades(html)
        news_url_list.extend(url_list)
        news_page_url = scrape_next_page_link(html)

    return news_url_list


def save_news_in_database(news):
    try:
        create_news(news)
    except pymongo.errors.ServerSelectionTimeoutError:
        print("Error ao cadastrar os dados!")


def get_tech_news(amount):
    news_url_list = get_news_url_list(amount)
    news_list = []

    for news_url in news_url_list:
        html = fetch(news_url)
        news = scrape_noticia(html)

        news_list.append(news)

        if len(news_list) == amount:
            break

    save_news_in_database(news_list)

    return news_list
