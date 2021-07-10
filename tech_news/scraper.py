import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        if (response.status_code != 200):
            return None
        return response.text
    except requests.ReadTimeout:
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    noticia = {}

    noticia['url'] = selector.css(
        "link[rel='canonical']::attr(href)"
    ).get()

    noticia['title'] = selector.css(
        "h1.tec--article__header__title::text"
    ).get()

    noticia['timestamp'] = selector.css("time::attr(datetime)").get()

    noticia['writer'] = selector.css(
        "a.tec--author__info__link::text"
    ).get()
    if noticia['writer'] is not None:
        noticia['writer'] = noticia['writer'].strip()

    noticia['shares_count'] = selector.css(
        "div.tec--toolbar__item::text"
    ).get()
    suffix = " Compartilharam"
    if noticia['shares_count']:
        noticia['shares_count'] = noticia['shares_count'][1:-len(suffix)]
        noticia['shares_count'] = int(noticia['shares_count'])
    else:
        noticia['shares_count'] = 0

    noticia['comments_count'] = selector.css(
        "button#js-comments-btn::attr(data-count)"
    ).get()
    noticia['comments_count'] = int(noticia['comments_count'])
    noticia["summary"] = "".join(
        selector.css("div.tec--article__body > p:first-child *::text").getall()
    )

    noticia["sources"] = list(map(
        str.strip, selector.css(".z--mb-16 div a.tec--badge::text").getall()
    ))

    noticia["categories"] = list(map(
        str.strip, selector.css("div#js-categories a::text").getall()
    ))

    return noticia


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(".tec--btn::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    noticias = []
    link_noticias = []
    html_novidades = fetch("https://www.tecmundo.com.br/novidades")
    link_noticias.extend(scrape_novidades(html_novidades))
    while len(link_noticias) < amount:
        novidades_next_page = scrape_next_page_link(html_novidades)
        html_novidades = fetch(novidades_next_page)
        link_noticias.extend(scrape_novidades(html_novidades))

    for link in link_noticias[:amount]:
        html_noticia = fetch(link)
        noticias.append(scrape_noticia(html_noticia))

    create_news(noticias)
    return noticias
