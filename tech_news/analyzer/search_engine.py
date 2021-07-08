from tech_news.database import search_news
import re


# Requisito 6
# https://docs.mongodb.com/manual/reference/operator/query/regex/
# https://stackoverflow.com/questions/5925731/reorder-dictionary-in-python-according-to-a-list-of-values/52044835
def search_by_title(title):
    """Seu código deve vir aqui"""
    items = search_news({'title': {'$regex': title, '$options': 'i'}})
    matches = [(item['title'], item['url']) for item in items]
    return matches


# Requisito 7
# https://stackoverflow.com/questions/22061723/regex-date-validation-for-yyyy-mm-dd/22061800
# https://docs.python.org/3/library/re.html
def search_by_date(date):
    """Seu código deve vir aqui"""
    rule = r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$'
    match = re.search(rule, date)
    if not match:
        return 'Data inválida'
    items = search_news({'timestamp': {'$regex': date, '$options': 'i'}})
    matches = [(item['title'], item['url']) for item in items]
    return matches


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    items = search_news({'sources': {'$regex': source, '$options': 'i'}})
    matches = [(item['title'], item['url']) for item in items]
    return matches


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    items = search_news({'categories': {'$regex': category, '$options': 'i'}})
    matches = [(item['title'], item['url']) for item in items]
    return matches
