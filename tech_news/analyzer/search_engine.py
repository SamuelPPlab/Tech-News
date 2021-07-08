from tech_news.database import search_news
import re
import datetime


# Requisito 6
def search_by_title(title):
    regex_filter = re.compile(f".*{title}.*", re.IGNORECASE)
    results = search_news({"title": regex_filter})
    news = []
    for result in results:
        a = (result["title"], result["url"])
        news.append(a)
    return news


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    else:
        regex = re.compile(f'.*{date}.*')
        results = search_news({"timestamp": regex})
        news = []
        for result in results:
            news_list = (result["title"], result["url"])
            news.append(news_list)
    return news


# Requisito 8
def search_by_source(source):
    news = []
    for source_item in source:
        regex = re.compile(f'.*{source_item}.*', re.IGNORECASE)
        results = search_news({"sources": regex})
        for result in results:
            news_list = (result["title"], result["url"])
            news.append(news_list)
        return news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
