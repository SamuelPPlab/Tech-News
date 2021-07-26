from tech_news.database import find_news
from collections import Counter


def sort_by_popularity(news):
    (title, url, popularity) = news
    return popularity


# Requisito 10
def top_5_news():
    news_all = find_news()

    def mapping(news_item):
        title = news_item.get("title")
        url = news_item.get("url")
        comments_count = news_item.get("comments_count")
        shares_count = news_item.get("shares_count")
        popularity = comments_count + shares_count
        return (title, url, popularity)

    news = list(map(mapping, news_all))

    news.sort(key=sort_by_popularity, reverse=True)

    filtered_list = []
    counter = 0
    while counter < 5 and counter < len(news):
        (title, url, popularity) = news[counter]
        filtered_list.append((title, url))
        counter += 1

    return filtered_list


# Requisito 11
def top_5_categories():
    news_all = find_news()

    categories_list = []
    
    for news in news_all:
        for category in news['categories']:
            categories_list.append(category)

    categories_and_qty = sorted(
        Counter(categories_list).most_common()
    )

    sorted_categories = []

    for category_and_qty in categories_and_qty:
        sorted_categories.append(category_and_qty[0])

    return sorted_categories[:5]
