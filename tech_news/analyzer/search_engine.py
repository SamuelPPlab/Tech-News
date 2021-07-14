from tech_news.database import search_news
import datetime


# https://qastack.com.br/programming/16870663/how-do-i-validate-a-date-string-format-in-python
def validate(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    find_title = search_news({'title': {'$regex': title, '$options': 'i'}})
    search = [
        (noticia['title'], noticia['url'])
        for noticia in find_title
    ]
    return search


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    validate(date)
    find_date = search_news({'timestamp': {'$regex': date}})
    search = [
        (noticia['title'], noticia['url'])
        for noticia in find_date
    ]
    return search


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    find_source = search_news({'sources': {'$regex': source, '$options': 'i'}})
    search = [
        (noticia['title'], noticia['url'])
        for noticia in find_source
    ]
    return search


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    find_category = search_news({
        'categories': {'$regex': category, '$options': 'i'}
        }
    )
    search = [
        (noticia['title'], noticia['url'])
        for noticia in find_category
    ]
    return search
