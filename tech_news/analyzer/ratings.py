from tech_news.database import find_news
from collections import Counter


def sort_by_popularity(news):
    (title, url, popularity) = news
    return popularity


def top_5_news():
    news_all = find_news()

    def mapping(item_news):
        title = item_news.get("title")
        url = item_news.get("url")
        comments_count = item_news.get("comments_count")
        shares_count = item_news.get("shares_count")
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


def top_5_categories():
    all_news = find_news()
    categories_list = []
    for news in all_news:
        for category in news['categories']:
            categories_list.append(category)
    categories_and_qty = sorted(
        Counter(categories_list).most_common()
    )
    sorted_categories = []
    for category_and_qty in categories_and_qty:
        sorted_categories.append(category_and_qty[0])
    return sorted_categories[:5]
