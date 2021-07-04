import requests
from time import sleep
import parsel

# Requisito 1
def fetch(url):
    sleep(1)

    try:
        response = requests.get(url, timeout=3)

        if response.status_code == 200:
            return response.text

        return None

    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    scrape_info = {}

    selector = parsel.Selector(html_content)

    scrape_info['url'] = selector.css("link[rel=canonical]::attr(href)").get()
    scrape_info['title'] = selector.css("h1::text").get()
    scrape_info['timestamp'] = selector.css("time::attr(datetime)").get()
    scrape_info['writer'] = selector.css(".tec--author__info__link::text").get().strip() if selector.css(".tec--author__info__link::text").get() else None
    scrape_info['shares_count'] = selector.css(".tec-toolbar__item::text").strip().split(' ')[0].get() if selector.css(".tec-toolbar__item::text") else 0
    scrape_info['comments_count'] = int(selector.css("button#js-comments-btn::attr(data-count)").get())
    scrape_info['summary'] = "".join(selector.css(".tec--article__body p:first-child *::text").getall())
    scrape_info['sources'] = [font.strip() for font in selector.css("h2:contains('Fontes') + div a::text").getall()]
    scrape_info['categories'] = [category.strip() for category in selector.css("div#js-categories a::text").getall()]
    

    return scrape_info

# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

# print(fetch('https://www.tecmundo.com.br/novidades'))
