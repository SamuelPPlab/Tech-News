from tech_news.database import find_news


# Requisito 6
def search_by_title(title):

    news_array = find_news()
    filtered_news = []
    for new in news_array:
        if new["title"].upper() == title.upper():
            filtered_news.append(new)
    if filtered_news:
        return [(new["title"], new["url"]) for new in filtered_news]
    else:
        return []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    news_array = find_news()
    filtered_news = []
    for new in news_array:
        for s in new["sources"]:
            if s.upper() == source.upper():
                filtered_news.append(new)
    if filtered_news:
        return [(new["title"], new["url"]) for new in filtered_news]
    else:
        return []


# Requisito 9
def search_by_category(category):
    news_array = find_news()
    filtered_news = []
    for new in news_array:
        for c in new["categories"]:
            if c.upper() == category.upper():
                filtered_news.append(new)
    if filtered_news:
        return [(new["title"], new["url"]) for new in filtered_news]
    else:
        return []
