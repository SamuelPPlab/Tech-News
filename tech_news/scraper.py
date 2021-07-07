import requests
from time import sleep
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        sleep(1)
        response = requests.get(url, timeout=3)
        return response.text if response.status_code == 200 else None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    noticia_info = {}

    selector = Selector(html_content)
    noticia_info["url"] = selector.xpath(
        "//html//head//meta[5]//@content"
    ).get()
    noticia_info["title"] = selector.css("#js-article-title::text").get()
    noticia_info["timestamp"] = selector.css(
        "#js-article-date::attr(datetime)"
    ).get()
    write_info = selector.css(
        "#js-author-bar > div > \
            p.z--m-none.z--truncate.z--font-bold > a::text"
    ).get()
    noticia_info["writer"] = (
        write_info.strip() if write_info is not None else None
    )
    shares_count = selector.css(
        "#js-author-bar > nav > div:nth-child(1)::text"
    ).get()
    noticia_info["shares_count"] = (
        int(shares_count[1:-15]) if shares_count is not None else 0
    )
    coments_count = selector.css("#js-comments-btn::attr(data-count)").get()

    noticia_info["comments_count"] = (
        int(coments_count) if coments_count is not None else 0
    )
    # Loucuras do Python \/ Nunca vi Join assim...
    noticia_info["summary"] = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )
    # HOF de map, str = string
    # sources = selector.css('a[rel="noopener nofollow"]::text').getall()

    noticia_info["sources"] = list(
        map(
            str.strip,
            selector.css('a[class=tec--badge]::text').getall(),
        )
    )

    noticia_info["categories"] = list(
        map(str.strip, selector.css("#js-categories > a::text").getall())
    )
    return noticia_info


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    novidade_list = selector.css(
        "#js-main > div > div > \
        div.z--col.z--w-2-3 > \
        div.tec--list.tec--list--lg > div > article > div > h3 > a::attr(href)"
    ).getall()

    return novidade_list


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    url = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 > \
         div.tec--list.tec--list--lg > a::attr(href)"
    ).get()
    return url


# Requisito 5
def get_tech_news(amount):
    news_url_tech_list = []
    url = "https://www.tecmundo.com.br/novidades"
    while len(news_url_tech_list) < amount:
        content = fetch(url)
        url_list = scrape_novidades(content)
        news_url_tech_list = news_url_tech_list + url_list
        del news_url_tech_list[amount::]
        url = scrape_next_page_link(content)
    # print(len(news_url_tech_list))
    tech_news_content_list = list(map(fetch, news_url_tech_list))
    tech_news_list = list(map(scrape_noticia, tech_news_content_list))
    create_news(tech_news_list)
    return tech_news_list
    # while news_url_tech_list
    """Seu código deve vir aqui"""
