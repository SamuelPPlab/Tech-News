import re
import requests
import time

from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if(response.status_code == 200):
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css('head link::attr(href)').getall()[20]
    title = selector.css('title::text').get().split("-")[0]
    times = selector.css('.tec--timestamp__item time::attr(datetime)').get()
    writer = selector.css('.z--m-none a::text').get().strip()
    shares_count = selector.css('.tec--toolbar__item::text').get()[1]
    comments_count = selector.css('.tec--btn::attr(data-count)').get()
    summary = selector.css('.tec--article__body p').get()
    sources = selector.css('.tec--badge::text').getall()
    categories = selector.css('#js-categories a::text').getall()

    new_categories = []
    new_sources = []
    new_sumary = re.sub('<[^>]+?>', '', summary)

    for categorie in categories:
        new_categories.append(categorie.strip())

    for source in sources:
        new_sources.append(source.strip())

    return {
        'url': url,
        'title': title.strip(),
        'timestamp': times,
        'writer': writer,
        'shares_count': int(shares_count),
        'comments_count': int(comments_count),
        'summary': new_sumary,
        'sources': new_sources,
        'categories': new_categories
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


# print("Resultado do fetch:\n")
# print(fetch("https://www.tecmundo.com.br/novidades"))
