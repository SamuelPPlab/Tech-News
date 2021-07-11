from tech_news.database import find_news


# Requisito 10
def top_5_news():
    db = find_news()
    list_popularity = [
        {
            "title": new["title"],
            "pop": new["comments_count"] + new["shares_count"],
            "url": new["url"],
        }
        for new in db
    ]

    list_sort_names = sorted(
        list_popularity, key=lambda i: (i["title"]), reverse=False
    )

    list_sort_age = sorted(
        list_sort_names, key=lambda i: (i["pop"]), reverse=True
    )

    limit_list = list_sort_age[:5]

    list_tuplas = [(new["title"], new["url"]) for new in limit_list]
    # print(limit_list)
    # print(list_tuplas)
    return list_tuplas


# top_5_news()


# Requisito 11
def top_5_categories():
    db = find_news()
    list_popularity = [
        {
            "title": new["title"],
            "pop": new["comments_count"] + new["shares_count"],
            "url": new["url"],
            "categories": new["categories"],
        }
        for new in db
    ]

    list_sort_names = sorted(
        list_popularity, key=lambda i: (i["title"]), reverse=False
    )

    list_sort_age = sorted(
        list_sort_names, key=lambda i: (i["pop"]), reverse=True
    )

    list(map(lambda new: new["categories"].sort(), list_sort_age))

    limit_list = list_sort_age[:5]
    # print(limit_list)

    list_categories1 = [new["categories"][0] for new in limit_list]
    list_categories2 = [new["categories"][1] for new in limit_list]
    list_categories1.extend(list_categories2)
    limit_categories = list_categories1[:5]
    # print("MINHA LISTA: ", limit_categories)
    return limit_categories


# top_5_categories()
