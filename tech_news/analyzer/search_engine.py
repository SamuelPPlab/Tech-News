import re
from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    new_info = search_news({"title": re.compile(title, re.IGNORECASE)})
    if len(new_info) < 1:
        return []
    return [(new_info[0]["title"], new_info[0]["url"])]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        splited_date = date.split("-")
        splited_date = [int(num) for num in splited_date]
        datetime(splited_date[0], splited_date[1], splited_date[2])
        new_info = search_news({"timestamp": re.compile(date)})
        if not new_info:
            return []
        return [(new_info[0]["title"], new_info[0]["url"])]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    new_info = search_news({"sources": re.compile(source, re.IGNORECASE)})
    if not new_info:
        return []
    return [(new_info[0]["title"], new_info[0]["url"])]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    new_info = search_news({"categories": re.compile(category, re.IGNORECASE)})
    if not new_info:
        return []
    return [(new_info[0]["title"], new_info[0]["url"])]
