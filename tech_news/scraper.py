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
    except requests.ReadTimeout as err:
        print(err)
        return None


"""Ajuda do colega Luiz Mariz para desenvolvimento do scrapper,
PR:
https://github.com/tryber/sd-07-tech-news/blob/
1397b9b65db700277f0f3886c75693a0ff81e5cb/tech_news/scraper.py"""
# Requisito 2


def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    selector = selector.css(".tec--article")

    initial_index = html_content.find("@id")
    last_index = html_content.find("}}", initial_index)
    url = html_content[(initial_index + 6):(last_index - 1)]

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
    next = selector.css("div.tec--list > a:last-child::attr(href)").get()

    if not next:
        return None
    return next


# Requisito 5
def get_tech_news_url(amount):
    url = "https://www.tecmundo.com.br/novidades"
    all_news = []

    while len(all_news) < amount:
        html = fetch(url)
        url_list = scrape_novidades(html)
        all_news.extend(url_list)
        url = scrape_next_page_link(html)

    return all_news


def save_news_in_db(news):
    try:
        create_news(news)
    except pymongo.errors.ServerSelectionTimeoutError:
        print("Erro para cadastrar os dados")


def get_tech_news(amount):
    news_url_list = get_tech_news_url(amount)
    all_news = []

    for news_url in news_url_list:
        html = fetch(news_url)
        news = scrape_noticia(html)

        all_news.append(news)

        if len(all_news) == amount:
            break

    save_news_in_db(all_news)

    return all_news
