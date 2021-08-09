from tech_news.database import get_collection


def top_5_news():
    db = get_collection().aggregate(
        [
            {
                "$project": {
                    "_id": 0,
                    "title": 1,
                    "url": 1,
                    "popularidade": {
                        "$add": ["$comments_count", "$shares_count"]
                    },
                }
            },
            {"$limit": 5},
        ]
    )

    result = []
    for item in db:
        result.append((item["title"], item["url"]))
    return result


def top_5_categories():
    db = get_collection().aggregate(
        [
            {"$unwind": "$categories"},
            {
                "$group": {
                    "_id": "$categories",
                }
            },
            {"$sort": {"_id": 1}},
            {"$limit": 5},
        ]
    )
    result = []
    for item in db:
        result.append(item["_id"])
    return result
