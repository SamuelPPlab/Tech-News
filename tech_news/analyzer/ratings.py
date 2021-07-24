from tech_news.database import find_news
from functools import reduce


# Requisito 10
def top_5_news():
    list =  sorted(
            find_news(),
            key=lambda field: (
                -(field["shares_count"] + field["comments_count"]),
                field["title"],
            ),
        )[:5]
    return [(news["title"], news["url"]) for news in list]


# Requisito 11
def top_5_categories():
    inf = [news_item["categories"] for news_item in find_news()]
    result = reduce(
        lambda news_list, current: [*news_list, *current],
        inf, [])
    counter = list()
    for category in result:
        counter.append((category, result.count(category)))
    counter.sort(key=lambda item: item[0])
    counter.sort(key=lambda item: item[1], reverse=True)
    top5 = [element[0] for element in counter][:5]
    return top5
