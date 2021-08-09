from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    array_of_found_news = search_news(query)

    all_news = []

    for news in array_of_found_news:
        title = news.get("title")
        url = news.get("url")

        all_news.append((title, url))

    return all_news


"""Dica do colega Luiz Mariz, foi utilizado consulta em PR:
https://github.com/tryber/sd-07-tech-news/blob/
1397b9b65db700277f0f3886c75693a0ff81e5cb/tech_news/analyzer/search_engine.py"""
# Requisito 7


def search_by_date(date):
    try:
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:])

        date = datetime.datetime(year=year, month=month, day=day)
        date = f"{date.date()}"
    except ValueError:
        raise ValueError("Data inválida")

    query = {"timestamp": {"$regex": date}}
    array_of_found_news = search_news(query)

    all_news = []
    for news in array_of_found_news:
        title = news.get("title")
        url = news.get("url")

        all_news.append((title, url))

    return all_news


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$regex": source, "$options": "i"}}
    array_of_found_news = search_news(query)

    all_news = []
    for news in array_of_found_news:
        title = news.get("title")
        url = news.get("url")

        all_news.append((title, url))

    return all_news


# Requisito 9
def search_by_category(category):
    query = {"categories": {"$regex": category, "$options": "i"}}
    array_of_found_news = search_news(query)

    all_news = []
    for news in array_of_found_news:
        title = news.get("title")
        url = news.get("url")

        all_news.append((title, url))

    return all_news
