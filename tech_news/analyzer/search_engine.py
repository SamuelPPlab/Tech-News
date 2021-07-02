import re
from tech_news.database import search_news


def filter_title_url(dict):
    return dict["title"], dict["url"]


def search(key, value):
    news = search_news({key: {"$regex": f"(?i){value}"}})
    return [filter_title_url(news) for news in news]


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    return search("title", title)


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    regex = r"^(20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$"
    if re.search(regex, date) is None:
        raise ValueError("Data inválida")
    return search("timestamp", date)


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    return search("sources", source)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    return search("categories", category)
