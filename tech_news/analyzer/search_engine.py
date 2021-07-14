from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    news = []
    for result in search:
        news.append((result['title'], result['url']))
    return news


# Requisito 7
def search_by_date(date):
    news = []
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    search = search_news({"timestamp": {"$regex": date}})
    for result in search:
        news_items = (result["title"], result["url"])
        news.append(news_items)
    return news


# Requisito 8
def search_by_source(source):
    search = search_news({"sources": {"$regex": source, "$options": "i"}})
    news = []
    for result in search:
        news.append((result['title'], result['url']))
    return news


# Requisito 9
def search_by_category(category):
    search = search_news({"categories": {"$regex": category, "$options": "i"}})
    news = []
    for result in search:
        news.append((result['title'], result['url']))
    return news
