from tech_news.database import db


# Requisito 10
def top_5_news():
    noticiasTop5 = list()
    noticiasBanco = list(
        db.news.aggregate(
            [
                {
                    "$addFields": {
                        "sort_order": {
                            "$add": ["$shares_count", "$comments_count"]
                        }
                    }
                },
                {"$sort": {"sort_order": -1}},
                {"$project": {"sort_order": 0}},
            ]
        )
    )
    if noticiasBanco:
        noticiasTop5 = [
            (noticias["title"], noticias["url"]) for noticias in noticiasBanco
        ][:5]
        return noticiasTop5
    else:
        return []


# Requisito 11
def top_5_categories():
    categoriasTop5 = list()
    categoriasBanco = db.news.aggregate(
        [
            {"$unwind": "$categories"},
            {"$sortByCount": "$categories"},
            {"$sort": {"count": -1, "_id": 1}},
            {"$project": {"category": "$_id"}},
            {"$limit": 5},
        ]
    )
    if categoriasBanco:
        categoriasTop5 = [
            (noticias["category"]) for noticias in categoriasBanco
        ]
        return categoriasTop5
    else:
        return []
