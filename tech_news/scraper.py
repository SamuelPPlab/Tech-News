import requests
import time
from parsel import Selector
import re
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        return response.text if response.status_code == 200 else None
    except requests.ReadTimeout:
        return None


# Requisito 2
"""Pega o resumo da notícia"""


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    writer = selector.css(".tec--author__info__link::text").get()
    if writer is not None:
        writer = writer.strip()
    shares = selector.css(".tec--toolbar__item::text").get()
    if shares is not None:
        shares = int(re.sub("[^0-9]", "", shares))
    else:
        shares = 0
    comments = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments is not None:
        comments = int(comments)
    summary = "".join(
        selector.css("div.tec--article__body p:nth-child(1) *::text").getall()
    )
    sources = selector.css("div.z--mb-16 a.tec--badge::text").getall()
    sources = [source.strip() for source in sources]
    categories = selector.css("div#js-categories a::text").getall()
    all_categories = [category.strip() for category in categories]
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares,
        "comments_count": comments,
        "summary": summary,
        "sources": sources,
        "categories": all_categories,
    }


# Requisito 3
"""Página de lista de notícias"""


def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urls = selector.css(".tec--list div h3 a::attr(href)").getall()
    return urls

# Requisito 4


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css(
        "a.tec--btn.tec--btn--lg::attr(href)"
    ).get()
    return next_page


# Requisito 5
"""Feito com a ajuda do Luiz E. F. Simões
assim como a refatoração dos outros requisitos acima."""


def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    all_urls = []

    while len(all_urls) < amount:
        response = fetch(url)
        all_urls.extend(scrape_novidades(response))
        url = scrape_next_page_link(response)

    group_notices = all_urls[:amount]
    notices_resume_list = []

    for notice in group_notices:
        resume_notice = scrape_noticia(fetch(notice))
        notices_resume_list.append(resume_notice)

    try:
        create_news(notices_resume_list)

    except Exception as error:
        print(error)

    return notices_resume_list
