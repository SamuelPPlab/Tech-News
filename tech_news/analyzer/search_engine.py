from tech_news.database import (
    search_news,
)
import datetime


# Requisito 6:
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {'title': {'$regex': '^' + title + '$', '$options': 'i'}}
    news_res = search_news(query)
    result = []
    if news_res is None:
        return result
    else:
        for new in news_res:
            item = (new['title'], new['url'])
            result.append(item)
        return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    else:
        query = query = {'timestamp': {'$regex': '^' + date}}
        news_res = search_news(query)
        result = []
        if news_res is None:
            return result
        else:
            for new in news_res:
                item = (new['title'], new['url'])
                result.append(item)
            return result


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    query = {
        'sources': {
            '$elemMatch': {
                '$regex': source,
                '$options': 'i'
            }
        }
    }
    news_res = search_news(query)
    result = []
    if news_res is None:
        return result
    else:
        for new in news_res:
            item = (new['title'], new['url'])
            result.append(item)
        return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    query = {
        'categories': {
            '$elemMatch': {
                '$regex': category,
                '$options': 'i'
            }
        }
    }
    news_res = search_news(query)
    result = []
    if news_res is None:
        return result
    else:
        for new in news_res:
            item = (new['title'], new['url'])
            result.append(item)
        return result
