from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    response = search_news(query)
    result = []
    for news in response:
        tupla_news = (news["title"], news["url"])
        result.append(tupla_news)
    return result


# search_by_title('novo Intel Core i7-1195G7 aparece em testes e surpreende')


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    query = {"timestamp": {"$regex": f"^{date}"}}
    response = search_news(query)
    result = []
    for news in response:
        tupla_news = (news["title"], news["url"])
        result.append(tupla_news)
    return result


# print(search_by_date('2020-11-23'))


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$elemMatch": {"$regex": source, "$options": "i"}}}
    response = search_news(query)
    result = []
    for news in response:
        tupla_news = (news["title"], news["url"])
        result.append(tupla_news)
    return result


# print(search_by_source('Resetera'))


# Requisito 9
def search_by_category(category):
    query = {
        "categories": {"$elemMatch": {"$regex": category, "$options": "i"}}
    }
    response = search_news(query)
    result = []
    for news in response:
        tupla_news = (news["title"], news["url"])
        result.append(tupla_news)
    return result


# print(search_by_category('console'))
