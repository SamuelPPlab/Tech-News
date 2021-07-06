# Requisito 1
import requests
from time import sleep
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout
from tech_news.database import create_news


def fetch(url):
    try:
        sleep(1)
        response = requests.get(url, timeout=3)
        return None if response.status_code != 200 else response.text
    except ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    bs = BeautifulSoup(html_content, "html.parser")
    url = bs.find("meta", property="og:url")
    title = bs.find("h1", id="js-article-title").get_text()
    timestamp = bs.find("time", id="js-article-date")
    writer = bs.find("a", class_="tec--author_info_link") or None
    shares_count = (
        bs.find("div", class_="tec--toolbar__item")
        .get_text()
        .strip()
    )
    comments_count = bs.find("button", id="js-comments-btn").get_text().strip()
    summary = (
        bs.find("div", class_="tec-article__body")
        .find("p")
        .get_text()
        .strip()
    )
    sources = bs.find("div", class_="z--mb-16")
    categories = (
        bs.find("div", class_="js-categories")
        .find_all("a", class_="tec--badge")
    )

    return {
        "url": url["content"],
        "title": title,
        "timestamp": timestamp["datetime"],
        "writer": None if writer is None else writer.get_text().strip(),
        "shares_count": int(
            "".join(s for s in shares_count[:3] if s.isdigit())
            ) if "Compartilharam" in shares_count else 0,
        "comments_count": int(
            "".join(s for s in comments_count if s.isdigit())
            ),
        "summary": summary,
        "sources": [t.get_text().strip() for t in sources.find_all("a")]
        if sources else [],
        "categories": [t.get_text().strip() for t in categories],
    }


# Requisito 3
def scrape_novidades(html_content):
    if html_content == '':
        return []

    bs = BeautifulSoup(html_content, "html.parser")

    AllItemsDiv = bs.find_all("div", class_="tec--list_item")

    return [div.find("a")["href"] for div in AllItemsDiv]


# Requisito 4
def scrape_next_page_link(html_content):
    if html_content == '':
        return None

    bs = BeautifulSoup(html_content, "html.parser")

    anchorElement = bs.find("a", class_="tec--btn--lg")

    return anchorElement["href"]


# Requisito 5
def get_tech_news(amount):
    if amount <= 0:
        return []
    tech_news_url = "https://tecmundo.com.br/novidades"
    tech_news = []
    while len(tech_news) < amount:
        news_page = fetch(tech_news_url)
        news_links = scrape_novidades(news_page)
        for news_item in news_links:
            news_url = fetch(news_item)
            tech_news.append(scrape_noticia(news_url))
            if len(tech_news) == amount:
                create_news(tech_news)
                return tech_news
        tech_news_url = scrape_next_page_link(news_page)
