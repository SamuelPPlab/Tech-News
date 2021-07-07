from typing import Collection
from tech_news.database import get_collection


def popularity(x):
    return (x['shares_count'] + x['comments_count'])


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    collection = get_collection().sort(key=popularity)[:5]
    return collection


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    collection = get_collection()
    dic = {}
    for item in collection:
        for sub_item in item.categories:
            if dic[sub_item]:
                dic[sub_item] = dic[sub_item] + 1
            else:
                dic[sub_item] = 1
    return sorted(collection.items(), key=lambda x: x[1])[:5]
