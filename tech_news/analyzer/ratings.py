from tech_news.database import find_news


# Requisito 10
def top_5_news():
    get_news = find_news()
    list_to_manipulate = []
    list_of_popularity = []
    for news in get_news:
        popularity = news["comments_count"] + news["shares_count"]
        new_info = {
            "title": news["title"],
            "url": news["url"],
            "popularity": popularity,
        }
        list_to_manipulate.append(new_info)
    newlist = sorted(
        list_to_manipulate, key=lambda k: k["popularity"], reverse=True
    )

    for item in newlist:
        item_nfo = (
            item["title"],
            item["url"],
        )
        list_of_popularity.append(item_nfo)
        if len(list_of_popularity) == 5:
            return list_of_popularity
    print(list_of_popularity)
    return list_of_popularity


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
