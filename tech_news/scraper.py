import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        # lance uma exceção caso o status não seja OK
        response.raise_for_status()
    except Exception as error:
        print(error)
        return None
    else:
        return response.text


# Requisito 2
def scrape_noticia(html_content):
    data = {}
    selector = Selector(text=html_content)

    data["url"] = selector.css(
        "head > meta[property='og:url']::attr(content)"
    ).get()

    data["title"] = selector.css("#js-article-title::text").get()

    data["timestamp"] = selector.css("time::attr(datetime)").get()

    if selector.css(".tec--author__info__link::text"):
        data["writer"] = (
            selector.css(".tec--author__info__link::text").get().strip()
        )
    else:
        data["writer"] = None
    # http://devfuria.com.br/python/strings/
    # Método strip() Retira espaços em branco no começo e no fim

    if selector.css(".tec--toolbar__item::text"):
        data["shares_count"] = int(
            selector.css(".tec--toolbar__item::text").get().split()[0]
        )
    else:
        data["shares_count"] = 0

    data["comments_count"] = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )

    data["summary"] = "".join(
        selector.css(
            "#js-main > div.z--container >"
            "article > div.tec--article__body-grid >"
            "div.tec--article__body > p:nth-child(1) *::text"
        ).getall()
    )

    # data["sources"] = []
    # for source in selector.css(".z--mb-16 div a.tec--badge::text").getall():
    #     data["sources"].append(source.strip())

    # Referencia: Estruturas de repetição, compreensão de listas, 34.1
    data["sources"] = [
        source.strip()
        for source in selector.css(".z--mb-16 div a.tec--badge::text").getall()
    ]

    data["categories"] = [
        category.strip()
        for category in selector.css(
            "#js-categories a.tec--badge::text"
        ).getall()
    ]
    return data


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    data = selector.css(
        ".tec--list__item .tec--card__thumb__link::attr(href)"
    ).getall()
    if len(data) == 0:
        return []
    else:
        return data


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("div.tec--list a.tec--btn::attr(href)").get()
    if next_page:
        return next_page
    else:
        return None


# Requisito 5
def get_tech_news(amount):
    news = []
    url = "https://www.tecmundo.com.br/novidades"

    while len(news) < amount:
        url_list = fetch(url)
        new_link = scrape_novidades(url_list)
        for item_list in new_link:
            list_noticias = fetch(item_list)
            news.append(scrape_noticia(list_noticias))
            if len(news) == amount:
                create_news(news)
                return news
        url = scrape_next_page_link(url_list)
# Referencias: Instrutores Tulio Olivieri e Maria Carolina req 2

# Referencias: Instrutores Maria Carolina req 5
# Tulio, Gleison e Lucival-T06 resolver conflito do re2 na tag do summary


# if __name__ == "__main__":
#     html_content = fetch(
#         'https://www.tecmundo.com.br/novidades'
#     )
#     print(scrape_novidades(html_content))
#     print(scrape_next_page_link(html_content))
