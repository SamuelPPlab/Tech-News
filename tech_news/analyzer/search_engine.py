# from pymongo.common import validate
from tech_news.database import search_news
import re


# Requisito 6
def search_by_title(title):
    searchQuery = {'title': {'$regex': f"{title}", '$options': 'i'}}
    tupleList = []

    result = search_news(searchQuery)
    for news in result:
        tupleNews = (news['title'], news['url'])
        tupleList.append(tupleNews)

    return tupleList


# Requisito 7
def search_by_date(date):
    # Regex pega do stack overflow
    validateRegex = re.search(
        "^[0-9]{4}[-/]?((((0[13578])|(1[02]))[-/]?(([0-2][0-9])|(3[01])))"
        + "|(((0[469])|(11))[-/]?(([0-2][0-9])|(30)))|(02[-/]?[0-2][0-9]))$",
        date
    )
    if (validateRegex is None):
        raise ValueError("Data inválida")

    searchQuery = {
        'timestamp': {
            '$regex': f"{date}T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]"
            }
        }
    tupleList = []

    result = search_news(searchQuery)
    for news in result:
        tupleNews = (news['title'], news['url'])
        tupleList.append(tupleNews)

    return tupleList


# Requisito 8
def search_by_source(source):
    searchQuery = {'sources': {'$regex': f"{source}", '$options': 'i'}}
    tupleList = []

    result = search_news(searchQuery)
    for news in result:
        tupleNews = (news['title'], news['url'])
        tupleList.append(tupleNews)

    return tupleList


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
