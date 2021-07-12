import re
import requests
import time

from tech_news.database import create_news
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=1)
        if(response.status_code == 200):
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


def remove_space(list):
    new_list = []
    for iten in list:
        new_list.append(iten.strip())
    return new_list


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css('head link::attr(href)').getall()[20]
    times = selector.css('.tec--timestamp__item time::attr(datetime)').get()
    comments_count = selector.css('.tec--btn::attr(data-count)').get()
    summary = "".join(
        selector.css('.tec--article__body > p:first-child *::text').getall()
    )
    sources = selector.css('.z--mb-16 a::text').getall()
    categories = selector.css('#js-categories a::text').getall()
    writer = (
        selector.css(".tec--author__info__link::text").get().strip()
        if selector.css('.tec--author__info__link::text').get() else None
    )
    new_categories = remove_space(categories)
    new_sources = remove_space(sources)

    if re.search("minha-serie", url):
        title = selector.css('title::text').get().split("| Minha Série")[0]
    elif re.search("voxel", url):
        title = selector.css('title::text').get().split("| Voxel")[0]
    else:
        shares_count = selector.css('.tec--toolbar__item::text').get()[1]
        title = selector.css('title::text').get().split('- TecMundo')[0]

    news_response = {
        'url': url,
        'title': title.strip(),
        'timestamp': times,
        'writer': writer,
        'comments_count': int(comments_count),
        'summary': summary,
        'sources': new_sources[0:len(new_sources)],
        'categories': new_categories
        }

    if re.search("minha-serie", url) or re.search('voxel', url):
        news_response['shares_count'] = int("0")
        return news_response
    else:
        news_response['shares_count'] = int(shares_count)
        return news_response


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_links = selector.css(".tec--card__info h3 a::attr(href)").getall()

    if len(news_links) == 0:
        return []
    else:
        return news_links


# Requisito 4
def scrape_next_page_link(html_content):
    try:
        selector = Selector(text=html_content)
        next_page_link = selector.css(".tec--btn::attr(href)").get()
        return next_page_link
    except next_page_link.DoesNotExist:
        return None


# Requisito 5
def get_tech_news(amount):
    html_text = fetch("https://www.tecmundo.com.br/novidades")
    links = []
    news = []
    while len(links) < amount:
        next_page = scrape_next_page_link(html_text)
        response = scrape_novidades(html_text)
        links.extend(response)
        if len(links) < amount:
            html_text = fetch(next_page)

    for link in links:
        news_data = scrape_noticia(fetch(link))
        news.append(news_data)

    create_news(news[:amount])
    return news[:amount]


# x = get_tech_news(30)
# print(x)
