import requests
import time
import parsel
from requests.exceptions import HTTPError, ReadTimeout


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if(response.status_code == 200):
            return response.text
    except ReadTimeout:
        return None

    except HTTPError:
        return None


# Requisito 2
def scrape_noticia(html_content):
    '''
    selector = parsel.Selector(html_content)
    article_selector = "article.tec--card"
    quotes = {}

    for quote in selector.css(article_selector).getall():
        selectorItens = parsel.Selector(quote)
        url = selectorItens.css("a.tec--card__title__link::attr(href)").get()
        title = selectorItens.css("a.tec--card__title__link::text").get()
        timestamp = selectorItens.css("div::attr(datetime)").get()
        print(timestamp)
        #response_selector = parsel.Selector(html_content+"/"+url)
        #writer = response_selector.css("div.tec--author__info").get()

        temporaryQuotes = {
          "url": url,
          "title": title,
        }

        quotes.update(temporaryQuotes)
        #print(quotes)
        break;
    '''


# Requisito 3
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    urls = selector.css("a.tec--card__title__link::attr(href)").getall()

    return urls or []


# Requisito 4
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    url = selector.css("a.tec--btn::attr(href)").get()

    return url or None


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
