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
    query_categorys = [
        {
          '$unwind': "$categories"
        },
        {
          '$group': {
            '_id': '$categories',
            'count': {
                '$sum': 1
                }
            }
        },
        {
          '$project': {
              '_id': 0,
              'category': '$_id',
              'count': 1
            }
        },
        {
          '$sort': {
            'count': -1,
            'category': 1
          }
        },
        {
          '$limit': 5
        }
    ]
    list_top_categories = []
    for item in db.news.aggregate(query_categorys):
        list_top_categories.append(item['category'])
    return list_top_categories
