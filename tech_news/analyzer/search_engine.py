from tech_news.database import search_news_with_fields
import datetime


def format_result(list):
    return [tuple(news.values()) for news in list]


def run_search_news_with_fields(key, value):
    query = {key: {"$regex": f"{value}", "$options": "i"}}
    print(query)
    fields = {"_id": 0, "title": "$title", "url": "$url"}
    return format_result(search_news_with_fields(query, fields))


# Requisito 6
def search_by_title(title):
    return run_search_news_with_fields("title", title)


# Requisito 7
def search_by_date(date):
    format = "%Y-%m-%d"
    try:
        datetime.datetime.strptime(date, format)
    except ValueError:
        raise ValueError("Data inválida")
    else:
        return run_search_news_with_fields("timestamp", date)


# Requisito 8
def search_by_source(source):
    return run_search_news_with_fields("sources", source)


# Requisito 9
def search_by_category(category):
    return run_search_news_with_fields("categories", category)
