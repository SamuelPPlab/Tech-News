from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = []
    get_news_by_title = search_news(
        {"title": {"$regex": title, "$options": "i"}})
    for news_info in get_news_by_title:
        news.append(tuple([news_info["title"], news_info["url"]]))
    return news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    year = date.split("-")[0]
    if int(year) < 2000 or len(year) != 4:
        raise ValueError("Data inválida")
    query = {"timestamp": {"$regex": f".*{date}.*"}}
    news_list = search_news(query)
    tuples_list = [(news["title"], news["url"]) for news in news_list]

    return tuples_list


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news = []
    get_news_by_source = search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )
    for news_info in get_news_by_source:
        news.append(tuple([news_info["title"], news_info["url"]]))
    return news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
