from tech_news.database import db


# Requisito 10
def top_5_news():
    query = [
        {
            '$project': {
                'popularity': {
                    '$add': ['$shares_count', '$comments_count']
                    },
                'title': 1,
                'url': 1,
                '_id': 0
            }
        },
        {
            '$sort': {
                'popularity': -1,
                'title': 1}
        },
        {
            '$limit': 5
        }
    ]
    list_news = []
    for new in db.news.aggregate(query):
        new_item = (new['title'], new['url'])
        list_news.append(new_item)
    return list_news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
