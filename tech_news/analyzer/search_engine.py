from tech_news.database import search_news
import re
import datetime

# Requisito 6


def search_by_title(title):
    # print(title) Vamoscomtudo
    pattern = re.compile(f'.*{title}.*', re.IGNORECASE)
    # print(pattern) VAMOSCOMTUDO
    results = search_news({"title": pattern})
    news = []
    for result in results:
        search = (result["title"], result["url"])
        news.append(search)
    return news

# Requisito 7


def search_by_date(date):
    # print(type(date))  <class 'str'>
    # https://docs.python.org/pt-br/3/library/datetime.html
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    else:
        rgx = re.compile(f'.*{date}.*')
        results = search_news({"timestamp": rgx})
        news = []
        for result in results:
            news_tupla = (result["title"], result["url"])
            news.append(news_tupla)
    return news

# Requisito 8


def search_by_source(source):
    news = []
    source_with_rg = re.compile(f'.*{source}.*', re.IGNORECASE)
    try:
        result = search_news({"sources": source_with_rg})
        if result is None:
            return []
    except ValueError:
        raise ValueError("Fonte inválida")
    else:
        for new in result:
            tupla = (new["title"], new["url"])
            news.append(tupla)
        return news

# Requisito 9


def search_by_category(category):
    """Seu código deve vir aqui"""
