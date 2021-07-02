from tech_news.database import find_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = find_news()
    result = []
    for new in news:
        if new["title"].upper() == title.upper():
            result.append(tuple([new["title"], new["url"]]))
    return result or []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    format_date = "%Y-%m-%d"
    try:
        datetime.strptime(date, format_date)  # Referência: Vanessa Bidinotto
        news = find_news()
        result = []
        for new in news:
            if new["timestamp"][0:10] == date:
                result.append(tuple([new["title"], new["url"]]))
        return result or []
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news = find_news()
    result = []
    for new in news:
        sources = []
        for s in new["sources"]:
            sources.append(s.upper())
        if source.upper() in sources:
            result.append(tuple([new["title"], new["url"]]))
    return result or []


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
