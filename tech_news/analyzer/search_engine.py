from tech_news.database import search_news
import datetime
# busquei a validação da data no PR do daniel Duarte


def search_by_title(title):
    db = search_news({'title': {'$regex': title, '$options': 'i'}})
    response = []

    if(len(db) > 0):
        for result in db:
            response.append((result['title', result['url']]))

    return response


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    db_result = search_news({'timestamp': {'$regex': date}})
    response = []

    for result in db_result:
        response.append((result['title', result['url']]))

    return response


def search_by_source(source):
    db_result = search_news({'source': {'$regex': source}})
    response = []

    for result in db_result:
        response.append((result['title', result['url']]))

    return response


def search_by_category(category):
    db_result = search_news({'categories': {'$regex': category}})
    response = []

    for result in db_result:
        response.append((result['title', result['url']]))

    return response
