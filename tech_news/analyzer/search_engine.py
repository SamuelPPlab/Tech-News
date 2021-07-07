from tech_news.database import get_collection, search_news


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


# search_by_title('elon')


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    found = get_collection().find({"datetime": date})
    output = []
    for item in list(found):
        print('entrou')
        output.append((item.title, item.url))
    print("output", output)
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
