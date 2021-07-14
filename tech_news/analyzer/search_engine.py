from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    info = list()
    news = search_news({"title": {"$regex": title, "$options": "si"}})
    for news_item in news:
        if news_item["title"]:
            get_tuple = (news_item["title"], news_item["url"])
            info.append(get_tuple)
    return info


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        info = list()
        news = search_news({"timestamp": {"$regex": date}})
        for news_item in news:
            get_tuple = (news_item["title"], news_item["url"])
            info.append(get_tuple)
        return info


# Requisito 8
def search_by_source(source):
    info = list()
    news = search_news({"sources": {"$regex": source, "$options": "si"}})
    for news_item in news:
        get_tuple = (news_item["title"], news_item["url"])
        info.append(get_tuple)
    return info


# Requisito 9
def search_by_category(category):
    info = list()
    news = search_news({"categories": {"$regex": category, "$options": "si"}})
    for news_item in news:
        get_tuple = (news_item["title"], news_item["url"])
        info.append(get_tuple)
    return info

# Referência:
# https://stackabuse.com/how-to-format-dates-in-python
