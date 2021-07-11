import requests
import time
import parsel


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        code = response.status_code

        if(code == 200):
            return response.text
        else:
            return None

    except requests.Timeout:
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
        #timestamp = selectorItens.css("div.tec--timestamp").get()

        response_selector = parsel.Selector(html_content+"/"+url)
        
        writer = response_selector.css("div.tec--author__info").get()

        print(writer)

        temporaryQuotes = {
          "url": url,
          "title": title,
        }

        quotes.update(temporaryQuotes)

        break;

        '''


# Requisito 3
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    article_selector = "article.tec--card"
    quotes = []

    for quote in selector.css(article_selector).getall():
        selectorItens = parsel.Selector(quote)
        url = selectorItens.css("a.tec--card__title__link::attr(href)").get()
        quotes.append(url)

    return quotes


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
