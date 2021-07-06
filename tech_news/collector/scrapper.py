import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.exceptions.RequestException:
        return ""
    else:
        return response.text


def get_article_elements(article_page):
    selectors = {
        "title": "#js-article-title::text",
        "timestamp": "time#js-article-date::attr(datetime)",
        "writer": "a.tec--author__info__link::text",
        "shares_count": ".tec--toolbar__item::text",
        "comments_count": "button#js-comments-btn::attr(data-count)",
        "summary": "div.tec--article__body p:first-of-type *::text",
        "sources": ".z--mb-16 a::text",
        "categories": "#js-categories a::text",
    }
    return {
        "title": article_page.css(selectors["title"]).get(),
        "timestamp": article_page.css(selectors["timestamp"]).get(),
        "writer": article_page.css(selectors["writer"]).get(),
        "shares_count": [
            int(s)
            for s in article_page.css(selectors["shares_count"])
            .get()
            .split(" ")
            if s.isdigit()
        ][0],
        "comments_count": int(
            article_page.css(selectors["comments_count"]).get()
        ),
        "summary": "".join(article_page.css(selectors["summary"]).getall()),
        "sources": article_page.css(selectors["sources"]).getall(),
        "categories": article_page.css(selectors["categories"]).getall(),
    }


def scrape(fetcher=fetch_content, pages=1):
    all_article_info = []
    for page in range(pages):
        url_all_news = f"https://www.tecmundo.com.br/novidades?page={page+1}"
        if page + 1 == 1:
            url_all_news = "https://www.tecmundo.com.br/novidades"

        news = fetcher(url_all_news)
        front_page = Selector(text=news)
        url_news = front_page.css(
            ".tec--list__item a.tec--card__title__link::attr(href)"
        ).getall()
        # print(url_news)
        for url in url_news:
            article_html = fetcher(url)
            article_page = Selector(text=article_html)
            # print(article_page.css("#js-article-title::text").get())
            elements = get_article_elements(article_page)
            elements["url"] = url
            all_article_info.append(elements)
            # print(elements)
    return all_article_info
