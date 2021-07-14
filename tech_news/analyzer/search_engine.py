from tech_news.database import search_news
import datetime

# Baseado no código do Arthur Massaini sobre como
# utilizar o regex em datas e importação do datetime.


# Requisito 6
def search_by_title(title):
    paginatedList = search_news(
        {"title": {"$regex": f"{title}", "$options": "i"}})
    return [(news["title"], news["url"]) for news in paginatedList]


# Requisito 7
def search_by_date(date):
    dateFormat = "%Y-%m-%d"
    try:
        datetime.datetime.strptime(date, dateFormat)  # Parse here
    except ValueError:
        raise ValueError("Data inválida")
    finally:
        paginatedList = search_news(
            {"timestamp": {"$regex": f"{date}", "$options": "i"}})
        return [(news["title"], news["url"]) for news in paginatedList]


# Requisito 8
def search_by_source(source):
    paginatedList = search_news(
        {"sources": {"$regex": f"{source}", "$options": "i"}})
    return [(news["title"], news["url"]) for news in paginatedList]


# Requisito 9
def search_by_category(category):
    paginatedList = search_news(
        {"categories": {"$regex": f"{category}", "$options": "i"}})
    return [(news["title"], news["url"]) for news in paginatedList]
