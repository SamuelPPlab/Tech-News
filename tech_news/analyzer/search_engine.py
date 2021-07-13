from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_list = []
    for news in search_news({"title": {"$regex": title, "$options": "i"}}):
        tupla = (news['title'], news['url'])
        news_list.append(tupla)
    return news_list


# Requisito 7 
def search_by_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        news_list = []
        for news in search_news({"timestamp": {
            "$regex": date, "$options": "x"
            }
        }):
            tupla = (news['title'], news['url'])
            news_list.append(tupla)
        return news_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news_list = []
    for news in search_news({"sources": {"$regex": source, "$options": "i"}}):
        tupla = (news['title'], news['url'])
        news_list.append(tupla)
    return news_list


# Requisito 9
def search_by_category(category):
    news_list = []
    for news in search_news({"categories": {
        "$regex": category, "$options": "i"
        }
    }):
        tupla = (news['title'], news['url'])
        news_list.append(tupla)
    return news_list
