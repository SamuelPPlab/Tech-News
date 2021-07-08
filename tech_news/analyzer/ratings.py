from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    pipeline = [
        {
            "$addFields": {
                "popularidade": {
                    "$sum": {"$add": ["$shares_count", "$comments_count"]}
                }
            }
        },
        {"$sort": {"popularidade": -1}},
        {"$limit": 5},
    ]
    news_db = list(get_collection().aggregate(pipeline))
    news_list = []
    for news in news_db:
        news_list.append((news["title"], news["url"]))
    return news_list


# Requisito 11
def top_5_categories():
    pipeline = [
        {"$unwind": "$categories"},
        {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        # {"$limit": 5},
    ]
    news_db = get_collection().aggregate(pipeline)
    news_list = []
    for news in news_db:
        news_list.append(news["_id"])
    if len(news_list) > 5:
        return sorted(news_list)[:5]
    return sorted(news_list)
