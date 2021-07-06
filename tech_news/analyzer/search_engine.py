from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    results = search_news({})
    result_tupla = []
    for result in results:
        if title.upper() == result["title"].upper():
            tupla = (result["title"], result["url"])
            result_tupla.append(tupla)

    return result_tupla


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        results = search_news({})
        result_tupla = []
        for result in results:
            time_list = result["timestamp"].split("T")
            if time_list[0] == date:
                tupla = (result["title"], result["url"])
                result_tupla.append(tupla)
    except ValueError:
        raise ValueError("Data inválida")

    return result_tupla


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    results = search_news({})
    result_tupla = []
    for result in results:
        upper_sources_list = []
        for a_source in result["sources"]:
            upper_sources_list.append(a_source.upper())
        if source.upper() in upper_sources_list:
            tupla = (result["title"], result["url"])
            result_tupla.append(tupla)

    return result_tupla


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    results = search_news({})
    result_tupla = []
    for result in results:
        upper_categories_list = []
        for a_category in result["categories"]:
            upper_categories_list.append(a_category.upper())
        if category.upper() in upper_categories_list:
            tupla = (result["title"], result["url"])
            result_tupla.append(tupla)

    return result_tupla
