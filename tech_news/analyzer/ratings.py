from tech_news.database import find_news


# Requisito 10
def top_5_news():
    responses = find_news()
    list_sorted = sorted(
        responses,
        key=lambda response: response["shares_count"]
        + response["comments_count"],
        reverse=True,
    )
    list = []
    limit = slice(5)
    for item in list_sorted:
        list.append((item["title"], item["url"]))
    return list[limit]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
