from tech_news.database import find_news
from operator import itemgetter
from collections import Counter

""" REF: https://docs.python.org/pt-br/dev/howto/sorting.html """


# Requisito 10
def top_5_news():
    allNews = find_news()

    orderAllNewsByName = sorted(allNews, key=itemgetter("title"))

    sortedAllNews = sorted(
        orderAllNewsByName,
        key=lambda news: news["shares_count"] + news["comments_count"],
        reverse=True,
    )

    tuple = []

    for news in sortedAllNews:
        tuple.append((news["title"], news["url"]))
    return tuple[:5]


# Requisito 11
def top_5_categories():
    allNews = find_news()
    allCategories = []

    for news in allNews:
        for category in news["categories"]:
            allCategories.append(category)

    commonCategories = Counter(allCategories).most_common()
    sortedCategories = sorted(commonCategories)

    tuple = []

    for cat in sortedCategories:
        tuple.append((cat[0]))
    return tuple[:5]
