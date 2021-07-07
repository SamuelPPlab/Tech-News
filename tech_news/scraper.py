import requests
import time
import pprint
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    if not url:
        print(f'Scapped site might be blocking request,\
             url being fetched:  {url}')
        return False
    else:
        try:
            time.sleep(3)
            res = requests.get(url, timeout=3)
            res.raise_for_status()
        except requests.exceptions.RequestException as error:
            print(error)
            return None
        else:
            return res.text


# Requisito 2
def scrape_noticia(html_content):
    # print(html_content)
    data = {}
    selector = Selector(html_content)
    data['url'] = selector.css(
        'head > meta[property="og:url"] ::attr(content)'
    ).get()
    data['title'] = selector.css('#js-article-title ::text').get()
    data['timestamp'] = selector.css(
        '#js-article-date ::attr(datetime)'
    ).get()
    writer = selector.css(
        '.tec--author__info__link ::text').get()
    data['writer'] = writer.strip() if writer else writer
    shares_count = selector.css(
        '.tec--toolbar__item ::text'
    ).get(default=0)
    if(shares_count and shares_count != ' '):
        data['shares_count'] = int(shares_count.strip('Compartilharam'))
    else:
        data['shares_count'] = 0
    comments_count = selector.css('#js-comments-btn\
         ::attr(data-count)').get()
    if(comments_count and comments_count != ' '):
        data['comments_count'] = int(comments_count)
    else:
        data['comments_count'] = 0
    data['summary'] = ''.join(selector.css(
        '.tec--article__body > p:first-child *::text'
    ).getall())
    data['sources'] = [item.strip(' ') for item in list(
        filter(lambda x: x != " ", selector.css(
            '.z--mb-16 .tec--badge ::text').getall())
    )]
    data['categories'] = [i.strip() for i in selector.css(
        '#js-categories a.tec--badge ::text'
    ).getall()]
    return(data)


# Requisito 3 i.strip(' ')
def scrape_novidades(html_content):
    if not html_content:
        return []
    return Selector(html_content).css(
        'h3 > .tec--card__title__link ::attr(href)').getall()


# Requisito 4
def scrape_next_page_link(html_content):
    extracted_data = Selector(html_content).css('.tec--btn ::attr(href)').get()
    return extracted_data


pp = pprint.PrettyPrinter(indent=4)


def handle_scrape_quantity(page_fetched, n_list):
    urls = scrape_novidades(page_fetched)
    if len(n_list) == 0:
        n_list = urls
    else:
        n_list.extend(urls)
    return n_list


def get_tech_news(amount):
    n_list = []
    scraped_data = []
    url = 'https://www.tecmundo.com.br/novidades'
    # content = fetch(url)
    while len(n_list) < amount:
        page_fetched = fetch(url)
        # print(page_fetched)
        if page_fetched:
            n_list = handle_scrape_quantity(page_fetched, n_list)
            url = scrape_next_page_link(page_fetched)
    if len(n_list) > 0:
        for link in n_list[:amount]:
            scraped_data.append(scrape_noticia(fetch(link)))
        create_news(scraped_data)
    return scraped_data


# fetched_news_data = fetch(
#     'https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm')


# fetched_data = fetch('https://www.tecmundo.com.br/novidades')
# print(scrape_noticia(fetched_news_data))
# pp.pprint(scrape_noticia(fetched_news_data))
# pp.pprint(scrape_next_page_link(fetched_data))
# pp.pprint(scrape_novidades(fetched_data))
# got_tec = get_tech_news(5)
# pp.pprint(got_tec)
# pp.pprint(len(got_tec))
