from parsel import Selector
import requests
import time

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    data = {}

    data["url"] = selector.css("link[rel=canonical]::attr(href)").get()

    data["title"] = selector.css(".tec--article__header__title::text").get()

    data["timestamp"] = selector.css("time::attr(datetime)").get()

    data["writer"] = selector.css("a.tec--author__info__link::text").get()

    if data["writer"]:
        data["writer"] = data["writer"].strip()

    shares = selector.css(".tec--toolbar__item::text").get()
    if shares:
        shares = int(shares.strip().split()[0])
    else:
        shares = 0
    data["shares_count"] = shares

    comments = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments:
        comments = int(comments)
    else:
        comments = 0
    data["comments_count"] = comments

    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    data["summary"] = "".join(summary)

    sources = selector.css(".z--mb-16 div a.tec--badge::text").getall()
    sources = [source.strip() for source in sources]
    data["sources"] = sources

    categories = selector.css("#js-categories a.tec--badge::text").getall()
    categories = [category.strip() for category in categories]
    data["categories"] = categories
    # print(data)
    return data


# scrape_noticia(
#     fetch(
#         "https://www.tecmundo.com.br/ciencia/215295-spacex-planeja-torre-captura-foguete-lancamento.htm"
#     )
# )


# Requisito 3
def scrape_novidades(html_content):
    try:
        selector = Selector(html_content)
        links = selector.css(
            "h3 a.tec--card__title__link::attr(href)"
        ).getall()
        return links
    except Exception:
        list()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    nextPage = selector.css(".tec--btn::attr(href)").get()
    return nextPage


# Requisito 5
def get_tech_news(amount):
    tecmundoUrl = "https://www.tecmundo.com.br/novidades"
    resultList = list()
    linksList = list()

    while len(linksList) < amount:
        tecmundoHTML = fetch(tecmundoUrl)
        linksList.extend(scrape_novidades(tecmundoHTML))
        tecmundoUrl = scrape_next_page_link(tecmundoHTML)

    for noticias in linksList[:amount]:
        resultList.append(scrape_noticia(fetch(noticias)))
    # print(resultList)
    create_news(resultList)
    return resultList
