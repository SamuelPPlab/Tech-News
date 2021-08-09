import pymongo
from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    cursor = get_collection().aggregate(
        [
            {
                "$project": {
                    "_id": False,
                    "title": True,
                    "url": True,
                    "popularidade": {
                        "$add": ["$comments_count", "$shares_count"]
                    },
                }
            },
            {"$limit": 5},
        ]
    )
    result = []
    for item in cursor:
        result.append((item["title"], item["url"]))
    return result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    cursor = get_collection().aggregate(
        [
            {"$unwind": "$categories"},
            {
                "$group": {
                    "_id": "$categories",
                }
            },
            {"$sort": {"_id": pymongo.ASCENDING}},
            {"$limit": 5},
        ]
    )
    result = []
    for item in cursor:
        result.append((item["_id"]))
    return result
