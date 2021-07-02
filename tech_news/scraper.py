import requests
import time
import pprint
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        res = requests.get(url, timeout=3)
        res.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(error)
        return None
    else:
        return res.text


# Requisito 2
def scrape_noticia(html_content):
    data = {}
    selector = Selector(html_content)
    data['url'] = selector.css(
        'head > meta[property="og:url"]::attr(content)'
    ).get()
    data['title'] = selector.css('#js-article-title ::text').get()
    data['timestamp'] = selector.css(
        '#js-article-date ::attr(datetime)'
    ).get()
    data['writer'] = selector.css(
        '.tec--author__info__link ::text').get().strip()
    data['shares_count'] = int(selector.css(
        '.tec--toolbar__item ::text'
    ).get().strip('Compartilharam'))
    data['comments_count'] = int(selector.css(
        '#js-comments-btn ::attr(data-count)'
        ).get())
    data['summary'] = ''.join(selector.css(
        '.tec--article__body > p:first-child ::text'
    ).getall())
    data['sources'] = [item.strip(' ') for item in list(
        filter(lambda x: x != " ", selector.css(
            '.z--mb-16 .tec--badge ::text').getall())
    )]
    data['categories'] = [item.strip(' ') for item in filter(
        lambda x: x != " ", list(
            selector.css('.z--px-16 #js-categories ::text').getall())
            )
        ]
    return(data)


# Requisito 3
def scrape_novidades(html_content):
    return Selector(html_content).css(
        '.tec--card__title__link ::attr(href)').getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


pp = pprint.PrettyPrinter(indent=4)
# fetched_data = fetch(
#     'https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm')

fetched_data = fetch('https://www.tecmundo.com.br/novidades')

pp.pprint(scrape_novidades(fetched_data))
