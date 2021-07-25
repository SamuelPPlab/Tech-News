# Requisito 6
from tech_news.database import find_news
from datetime import datetime
from tech_news.database import search_news


def search_by_title(title):

    list_news = find_news()

    return [
        (news["title"], news["url"])
        for news in list_news if title.lower() in news["title"].lower()
    ]


# Requisito 7
def search_by_date(date):

    try:
        datetime.strptime(date, "%Y-%m-%d")
        news_list = search_news({"timestamp": {"$regex": date}})
        return [(news["title"], news["url"]) for news in news_list]

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = find_news()
    return [
        (new["title"], new["url"])
        for new in news if find_source_news(new, source)
    ]


def find_source_news(new, source):
    for source_new in new["sources"]:
        if source.lower() != source_new.lower():
            return False
    return True


# Requisito 9
def search_by_category(category):
    news = find_news()
    return [
        (new["title"], new["url"])
        for new in news if find_category_news(new, category)
    ]


def find_category_news(new, category):
    for category_new in new["categories"]:
        if category.lower() == category_new.lower():
            return True
    return False
