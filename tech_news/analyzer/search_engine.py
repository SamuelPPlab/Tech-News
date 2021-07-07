from tech_news.database import get_collection, search_news
import re


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    found = get_collection().find(
        {"title": {"$regex": title, "$options": "-i"}}
    )
    found = list(found)
    result = []
    for item in found:
        result.append((item["title"], item["url"]))
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    test = re.search(
        "^20[0-2][0-9]-((0[1-9])|(1[0-2]))-([0-2][1-9]|3[0-1])$", date)
    if not test:
        raise ValueError('Data inválida')
    else:
        # found = list(get_collection().find({"timestamp": date}))
        found = get_collection().find(
            {"timestamp": {"$regex": date, "$options": "-i"}})
        print('found', found)
        output = []
        for item in found:
            print('entrou')
            output.append((item["title"], item["url"]))
        # print("output", output)
        return output


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    found = search_news({source: source})
    output = []
    for item in found:
        output.append((item.title, item.url))
    return output or []


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    found = search_news({category: category})
    output = []
    for item in found:
        output.append((item.title, item.url))
    return output or []
