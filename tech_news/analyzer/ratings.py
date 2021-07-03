from tech_news.database import db


# Requisito 10
def top_5_news():
    data = db.news.aggregate([
        {"$addFields": {
         "popularity": {
              "$sum": {"$sum": ["$comments_count", "$shares_count"]}
            },
         }},
        {"$sort": {"popularity": -1}},
        ]
        )
    result = []
    for news in list(data):
        info = (news["title"], news["url"])
        result.append(info)
    if(len(result) < 5):
        return list(result)
    return list(result)[:5]


# Requisito 11
def top_5_categories():
    data = db.news.aggregate(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "amount": {"$sum": 1}}},
            {"$sort": {"_id": 1}},
        ]
        )
    result = list(map(lambda x: x["_id"], list(data)))
    if(len(result) < 5):
        return result
    return result[:5]
