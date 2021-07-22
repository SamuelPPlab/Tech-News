from tech_news.database import search_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    result = search_news({})

    ordered = sorted(
        result,
        key=itemgetter('shares_count', 'comments_count'),
        reverse=True
        )[:5]
    list_of_news = []

    for new in ordered:
        list_of_news.append((new['title'], new['url']))

    return list_of_news


# Requisito 11
def top_5_categories():
    result = search_news({})

    list_of_categories = []

    for category in result:
        list_of_categories += category['categories']

    list_of_category_dicts = []

    for category in list_of_categories:
        category_dict = {
            'category': category,
            'repetitions': list_of_categories.count(category)
            }
        list_of_category_dicts.append(category_dict)

    ordered = sorted(
        list_of_category_dicts,
        key=itemgetter('repetitions', 'category')
        )[:5]

    final_list = []

    for category_dict in ordered:
        final_list.append(category_dict['category'])

    return final_list
