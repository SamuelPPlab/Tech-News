from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": f".*{title}*.", "$options": "-i"}}
    news_list = search_news(query)
    tuples_list = [(news["title"], news["url"]) for news in news_list]

    return tuples_list


# Requisito 7
def search_by_date(date):
    year = date.split("-")[0]
    if int(year) < 2000 or len(year) != 4:
        raise ValueError("Data inválida")
    query = {"timestamp": {"$regex": f".*{date}.*"}}
    news_list = search_news(query)
    tuples_list = [(news["title"], news["url"]) for news in news_list]

    return tuples_list


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$regex": f".*{source}*.", "$options": "i"}}
    news_list = search_news(query)
    tuples_list = [(news["title"], news["url"]) for news in news_list]

    return tuples_list


# Requisito 9
def search_by_category(category):
    query = {"categories": {"$regex": f".*{category}*.", "$options": "i"}}
    news_list = search_news(query)
    tuples_list = [(news["title"], news["url"]) for news in news_list]

    return tuples_list
