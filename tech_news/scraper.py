import requests
from time import sleep
from parsel import Selector


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
    write_info = (
        selector.css(
            "#js-author-bar > div > \
            p.z--m-none.z--truncate.z--font-bold > a::text"
        )
        .get()
        .strip()
    )
    noticia_info["writer"] = write_info if write_info is not None else None
    shares_count = int(
        selector.css("#js-author-bar > nav > div:nth-child(1)::text").get()[
            1:-15
        ]
    )
    noticia_info["shares_count"] = (
        shares_count if shares_count is not None else 0
    )
    coments_count = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )
    noticia_info["comments_count"] = (
        coments_count if coments_count is not None else 0
    )
    # Loucuras do Python \/ Nunca vi Join assim...
    noticia_info["summary"] = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )
    # HOF de map, str = string
    noticia_info["sources"] = list(
        map(
            str.strip,
            selector.css(
                "#js-main > div.z--container > \
                article > div.tec--article__body-grid > \
                div.z--mb-16.z--px-16 > div > a::text"
            ).getall(),
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
    """Seu código deve vir aqui"""
