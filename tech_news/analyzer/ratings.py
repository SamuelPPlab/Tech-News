from tech_news.database import db


# Requisito 10
def top_5_news():
    result = []
    response = db.news.aggregate(
        [
            {
                "$addFields": {
                    "popularity": {
                        "$add": ["$shares_count", "$comments_count"]
                    }
                }
            },
            {"$sort": {"popularity": -1, "title": 1}},
            {"$limit": 5},
        ]
    )
    for news in response:
        tupla_news = (news["title"], news["url"])
        result.append(tupla_news)
    return result


# print(top_5_news())


# Requisito 11
def top_5_categories():
    result = []
    response = db.news.aggregate(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "totalCategories": {"$sum": 1}}},
            {"$sort": {"totalCategories": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )
    for news in response:
        result.append(news['_id'])
    return result


# print(top_5_categories())
