from tech_news.database import find_news
from collections import Counter


# https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
# Mario F e Boris
# Gleison e Carol
# Requisito 10
def top_5_news():
    response = find_news()

    if len(response) == 0:
        return response

    news_list_with_order = []
    for news in response:
        news['order'] = int(news['shares_count']) + int(news['comments_count'])
        news_list_with_order.append(news)

    sorted_list = sorted(
        news_list_with_order, key=lambda curr_key: (
            curr_key['title'], curr_key['order']
        )
    )[:5]

    return [(news['title'], news['url']) for news in sorted_list]


# Requisito 11
# Caputo
def top_5_categories():
    news_list = find_news()

    categories_list = []
    sorted_categories = []

    for news in news_list:
        for category in news['categories']:
            categories_list.append(category)

    categories_and_qty = sorted(Counter(categories_list).most_common())

    for category_and_qty in categories_and_qty:
        sorted_categories.append(category_and_qty[0])

    return sorted_categories[:5]
