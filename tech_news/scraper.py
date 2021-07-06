import parsel
import requests
import time
import re


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
def scrape_noticia(html_content: str):
    selector = parsel.Selector(html_content)
    selector = selector.css(".tec--article")

    start_index = html_content.find(""""@id":""")
    end_index = html_content.find("}}", start_index)
    url = html_content[(start_index + 7):(end_index - 1)]

    title = selector.css("#js-article-title::text").get()

    timestamp = selector.css("time#js-article-date::attr(datetime)").get()

    writer = selector.css("a.tec--author__info__link::text").get()
    writer = writer.strip()

    shares_count = selector.css("div.tec--toolbar__item::text").re_first(r"\d")
    shares_count = int(shares_count)

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    comments_count = int(comments_count)

    summary = selector.css(".tec--article__body p:first-child").get()
    summary = re.sub(r"<[^>]*>", "", summary)

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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
