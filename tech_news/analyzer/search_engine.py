from tech_news.database import search_news
import re
from datetime import datetime


def format_results(list):
    return [(result['title'], result['url']) for result in list]


# Requisito 6
def search_by_title(title):
    """Faz buscas nas notícias por título no DB"""
    query = {'title': {'$regex': title, '$options': 'i'}}
    results_raw = search_news(query)
    results = format_results(results_raw)
    return results


# Requisito 7
def search_by_date(date):
    """Faz buscas nas notícias por data no DB"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except Exception:
        raise ValueError('Data inválida')

    query = {'timestamp': {'$regex': date}}
    results_raw = search_news(query)
    results = format_results(results_raw)
    return results


# Requisito 8
def search_by_source(source):
    """Faz buscas nas notícias por fonte no DB"""
    try:
        search = source.lower()
    except AttributeError:
        print('Please use a valid string.')
        return None

    regex = re.compile(rf'{search}', re.IGNORECASE)
    query = {'sources': {'$in': [regex]}}
    results_raw = search_news(query)
    results = format_results(results_raw)
    return results


# Requisito 9
def search_by_category(category):
    """Faz buscas nas notícias por categorias no DB"""
    try:
        search = category.lower()
    except AttributeError:
        print('Please use a valid string.')
        return None

    regex = re.compile(rf'{search}', re.IGNORECASE)
    query = {'categories': {'$in': [regex]}}
    results_raw = search_news(query)
    results = format_results(results_raw)
    return results
