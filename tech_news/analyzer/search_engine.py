import tech_news.database as db
import re

# Requisito 6


def search_by_title(title):
    news_list = db.search_news(
        {"title": {"$regex": re.compile(title, re.IGNORECASE)}}
    )
    news_tuple_list = list(
        map(lambda news: (news["title"], news["url"]), news_list)
    )

    return news_tuple_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
