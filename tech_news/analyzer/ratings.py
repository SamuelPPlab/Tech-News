from tech_news.database import db

"""Queries feitas com ajuda"""
news_lista = [
    {
        "$project": {
            "title": 1,
            "url": 1,
            "popularity": {"$sum": ["$shares_count", "$comments_count"]},
            "_id": 0,
        }
    },
    {"$sort": {"popularity": -1, "title": 1}},
    {"$limit": 5},
]

categories_lista = [
    {"$unwind": "$categories"},
    {"$group": {"_id": "$categories", "total": {"$sum": 1}}},
    {"$sort": {"total": -1, "_id": 1}},
    {"$limit": 5},
    {"$project": {"category": "$_id", "total": 1, "_id": 0}},
]


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    top_five = db.news.aggregate(news_lista)
    top_five_list = []
    for news in top_five:
        top_five_list.append((news["title"], news["url"]))
    return top_five_list


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    top_five = db.news.aggregate(categories_lista)
    top_five_list = []
    for news in top_five:
        top_five_list.append(news["category"])
    return top_five_list
