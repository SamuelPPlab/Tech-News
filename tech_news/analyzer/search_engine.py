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
# https://stackoverflow.com/questions/1711727/regular-expression-to-match-dates-in-yyyy-mm-dd-format
# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/tutorial/errors.html
def search_by_date(date):
    """Seu código deve vir aqui"""
    rule = r'^20[0-2][0-9]-((0[1-9])|(1[0-2]))-([0-2][1-9]|3[0-1])$'
    match = re.search(rule, date)
    if match is None:
        raise ValueError('Data inválida')
    items = search_news({'timestamp': {'$regex': date}})
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
