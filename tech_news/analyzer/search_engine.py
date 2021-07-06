# Requisito 6
from tech_news.database import search_news


def search_by_title(title):
    find_query = {"title": {"$regex": title, "$options": "i"}}
    news_search = search_news(find_query)
    news_list = []
    for news in news_search:
        news_list.append((news["title"], news["url"]))
    return news_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


print(search_by_title("Felipe"))
