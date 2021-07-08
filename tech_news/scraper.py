import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except Exception:
        return None


# Requisito 2
def scrape_noticia(html_content):

    result = {}

    content = Selector(html_content)

    body_grid = "#js-main > \
        div.z--container > \
        article > \
        div.tec--article__body-grid"

    result["url"] = content.xpath('//html//head//meta[5]//@content').get()
    result["title"] = content.css(".tec--article__header__title::text").get()
    result["timestamp"] = content.css("#js-article-date::attr(datetime)").get()
    result["writer"] = content.css("\
        .tec--author__info__link::text\
            ").get(default='None').strip()
    result["shares_count"] = int(content.xpath('\
        //*[@id="js-author-bar"]//nav//div[1]//text()\
            ').get(default='0').strip()[:-15])
    result["comments_count"] = int(content.css("\
        #js-comments-btn::attr(data-count)").get())
    result["summary"] = "".join(content.css(f"\
         {body_grid} > div.tec--article__body.z--px-16.p402_premium \
             > p:nth-child(1) *::text").getall())
    result["sources"] = list(map(str.strip, content.css(f"\
         {body_grid}> div.z--mb-16.z--px-16 > div > ::text").getall()))
    result["categories"] = list(map(str.strip, content.css("\
        #js-categories > ::text").getall()))
    return result


# Requisito 3

def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
