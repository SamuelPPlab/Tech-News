import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    html = Selector(html_content)
    res = {}
    res["url"] = html.css('meta[property="og:url"]::attr(content)').get()
    res["title"] = html.css(
        'meta[property="og:title"]::attr(content)').get().strip()
    res["timestamp"] = html.css('time::attr(datetime)').get().strip()
    res["writer"] = html.css(".tec--author__info__link::text").get().strip()
    res["shares_count"] = (
        int(html.css(".tec--toolbar__item::text").get().strip()[:2])
        if html.css(".tec--toolbar__item::text")
        else 0)
    res["comments_count"] = int(
        html.css("#js-comments-btn::attr(data-count)").get())
    res["summary"] = "".join(
        html.css(".tec--article__body > p:first-child *::text").getall())
    res["sources"] = [
        source.strip()[9:]
        for source in html.css(".z--mb-16 a.tec--badge::attr(title)").getall()]
    res["categories"] = [
        cat.strip()[9:]
        for cat in html.css(".tec--badge--primary::attr(title)").getall()]
    print(res)
    return res


# Requisito 3
def scrape_novidades(html_content):
    html = Selector(html_content)
    return html.css(
        'h3 .tec--card__title__link::attr(href)').getall()


# Requisito 4
def scrape_next_page_link(html_content):
    html = Selector(html_content)
    return html.css(
        '.z--mt-48::attr(href)').get()


# Requisito 5
def get_tech_news(amount):
    novidades = scrape_novidades(
        fetch("https://www.tecmundo.com.br/novidades"))
    