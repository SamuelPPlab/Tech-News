from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    news_found = find_news()

    news_popularity = [
        (news['shares_count'] + news['comments_count'],
            news['title'], news['url'])
        for news in news_found
    ]

    news_popularity_sorted = sorted(news_popularity, key=lambda var: var[1])
    news_popularity_sorted = sorted(
        news_popularity, key=lambda var: var[0], reverse=True)

    top_five_popularity = []

    for news in news_popularity_sorted:
        news_keys = (news[1], news[2])
        top_five_popularity.append(news_keys)

    return top_five_popularity[:5]

# Thays Costa e Gleison


# Requisito 11
def top_5_categories():
    news_found = find_news()

    all_categories = []

    for news in news_found:
        all_categories.extend(news['categories'])

    news_categories_sorted = sorted(all_categories)
    all_categories_count = Counter(news_categories_sorted).most_common()

    all_categories_sorted = [category[0] for category in all_categories_count]

    if len(all_categories_sorted) < 5:
        return all_categories_sorted
    else:
        return all_categories_sorted[:5]

# https://www.geeksforgeeks.org/python-accessing-nth-element-from-tuples-in-list/
# https://www.kite.com/python/answers/how-to-sort-a-%60counter%60-object-by-count-in-python
