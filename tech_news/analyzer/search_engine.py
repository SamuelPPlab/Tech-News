from tech_news.database import search_news
import re
import datetime

# Requisito 6


def return_general(results):
    news = []
    for result in results:
        search = (result["title"], result["url"])
        news.append(search)
    return news


def results_is_none(results):
    if results is None:
        return []


def search_by_title(title):
    pattern = re.compile(f'.*{title}.*', re.IGNORECASE)
    try:
        results = search_news({"title": pattern})
    except ValueError:
        raise ValueError("Titulo inválido")
    else:
        results_is_none(results)
        return return_general(results)

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
        results_is_none(results)
        return return_general(results)

# Requisito 8


def search_by_source(source):
    source_with_rg = re.compile(f'.*{source}.*', re.IGNORECASE)
    try:
        results = search_news({"sources": source_with_rg})
        results_is_none(results)
    except ValueError:
        raise ValueError("Fonte inválida")
    else:
        return return_general(results)

# Requisito 9


def search_by_category(category):
    category_with_rg = re.compile(f'.*{category}.*', re.IGNORECASE)
    try:
        results = search_news({"categories": category_with_rg})
        results_is_none(results)
    except ValueError:
        raise ValueError('Categoria inválida')
    else:
        return return_general(results)
