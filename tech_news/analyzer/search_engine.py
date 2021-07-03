from tech_news.database import db
import datetime
import re


# Requisito 6
def search_by_title(title):
    rgx = re.compile(f'.*{title}.*', re.IGNORECASE)
    data = list(db.news.find({'title': rgx}))
    result = []
    for news in data:
        info = (news["title"], news["url"])
        result.append(info)
    return result


# Requisito 7
def search_by_date(date):
    try:
        date_formated = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        rgx = re.compile(f'.*{date_formated}.*', re.IGNORECASE)
        data = list(db.news.find({'timestamp': rgx}))
        result = []
        for news in data:
            info = (news["title"], news["url"])
            result.append(info)
        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    data = db.news.find({})
    result = []
    for news in data:
        for source_data in news["sources"]:
            if(source_data.lower() == source.lower()):
                info = (news["title"], news["url"])
                result.append(info)
    return result


# Requisito 9
def search_by_category(category):
    data = db.news.find({})
    result = []
    for news in data:
        for category_data in news["categories"]:
            if(category_data.lower() == category.lower()):
                info = (news["title"], news["url"])
                result.append(info)
    return result
