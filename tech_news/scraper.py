import requests, time
from parsel import Selector

# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except Exception as error:
        print("Error: ", error)
        return None
    else:
        return response.text


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    news = {}
    selector = Selector(html_content)
    news["url"] = selector.css("meta[property='og:url']::attr(content)").get()
    news["title"] = selector.css("#js-article-title::text").get()
    news["timestamp"] = selector.css("#js-article-date::attr(datetime)").get()
    news["writer"] = (
        selector.css(".tec--author__info__link::text").get().strip()
    )
    news["shares_count"] = int(
        selector.css(".tec--toolbar__item::text")
        .get()
        .removesuffix("Compartilharam")
    )
    news["comments_count"] = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )
    news["summary"] = "".join(
        selector.css(".tec--article__body p:first-child *::text").getall()
    )
    news["sources"] = list(
        map(
            str.strip,
            selector.css('a[rel="noopener nofollow"]::text').getall(),
        )
    )
    news["categories"] = list(
        map(str.strip, selector.css("#js-categories > ::text").getall())
    )
    return news


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


noticia_html = fetch(
    "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
)

print(scrape_noticia(noticia_html))