from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    titleRegex = {"$regex": title, "$options": "i"}
    results = search_news({"title": titleRegex})
    newsList = []
    for result in results:
        newsInfo = (result["title"], result["url"])
        newsList.append(newsInfo)
    return newsList


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        dateRegex = {"$regex": date}
        results = search_news({"timestamp": dateRegex})
    except ValueError:
        raise ValueError('Data inválida')
    
    newsList = []
    for result in results:
        newsInfo = (result["title"], result["url"])
        newsList.append(newsInfo)
    return newsList


# Requisito 8
def search_by_source(source):
    sourceRegex = {"$regex": source, "$options": "i"}
    results = search_news({"sources": sourceRegex})
    newsList = []
    for result in results:
        newsInfo = (result["title"], result["url"])
        newsList.append(newsInfo)
    return newsList


# Requisito 9
def search_by_category(category):
    categoryRegex = {"$regex": category, "$options": "i"}
    results = search_news({"categories": categoryRegex})
    newsList = []
    for result in results:
        newsInfo = (result["title"], result["url"])
        newsList.append(newsInfo)
    return newsList
