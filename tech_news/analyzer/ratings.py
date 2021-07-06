from tech_news import database


def return_title_url(news):
    result = []
    for single_news in news:
        result.append((single_news["title"], single_news["url"]))
    return result


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news = database.aggregate_most_engage()
    return return_title_url(news)


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    news = database.top_5_categories()
    if len(news) == 0:
        return []
    print(news)
    print([obj["categories"] for obj in news])
    return [obj["categories"] for obj in news]
