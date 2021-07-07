from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    low_title = title.lower()
    found = search_news({title: low_title})
    output = []
    for item in found:
        output.append((item.title, item.url))
    return output or []


# search_by_title('elon')


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    found = search_news({date: date})
    output = []
    for item in found:
        output.append((item.title, item.url))
    return output or []


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
