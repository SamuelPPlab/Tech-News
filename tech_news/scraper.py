import requests
import time
from parsel import Selector
from tech_news.database import create_news
from math import ceil


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        if (response.status_code != 200):
            return None
        return response.text
    except requests.Timeout:
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    links = selector.css('link').getall()
    for link in links:
        if ('canonical' in link):
            url_news = link
            index = url_news.index('href="')
            url_news = url_news[index+6:len(url_news)-2]

    title = selector.css('#js-article-title::text').get()
    timestamp = selector.css('#js-article-date::attr(datetime)').get()
    writer = selector.css('.tec--author__info__link::text').get()
    if writer is not None:
        writer = writer.strip()

    shares = (selector.css('.tec--toolbar__item::text').get())
    if shares is not None:
        shares.lstrip()
        shares_count = int(shares[0:shares.index('C')-1])
    else:
        shares_count = 0

    prop_comments = '#js-comments-btn::attr(data-count)'
    comments_count = int(selector.css(prop_comments).get())
    prop_summary = '#js-main > div.z--container > article > '
    'div.tec--article__body-grid > div.tec--article__body > '
    'p:nth-child(1) *::text'
    summary = ''.join(selector.css(
        prop_summary
    ).getall())
    sources = selector.css('.z--mb-16 div a::text').getall()
    sources = [word.strip() for word in sources]

    categories = selector.css('#js-categories a::text').getall()
    categories = [word.strip() for word in categories]

    return {
        "url": url_news,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    new_selector = Selector(text=html_content)
    urls = []
    for item in new_selector.css('.tec--list__item'):
        url = item.css('h3 a::attr(href)').get()
        urls.append(url)
    return urls


# Requisito 4
def scrape_next_page_link(html_content):
    new_selector_next = Selector(text=html_content)
    next_page = new_selector_next.css('.tec--btn::attr(href)').get()
    return next_page


# Requisito 5
def get_tech_news(amount):
    url_news = 'https://www.tecmundo.com.br/novidades'
    array_news = []
    number_of_pages = (ceil(amount % 20)+amount) // 20
    print(number_of_pages)
    index = 0
    while index < number_of_pages:
        html_content = fetch(url_news)
        itens_urls = scrape_novidades(html_content)

        for url_item in itens_urls:
            new_html_content = fetch(url_item)
            print(url_item)
            if len(array_news) < amount:
                news = scrape_noticia(new_html_content)
                array_news.append(news)
        index += 1
        url_news = scrape_next_page_link(html_content)
    create_news(array_news)
    return array_news
