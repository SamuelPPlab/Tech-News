from tech_news.database import get_collection

# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    
    cursor = get_collection().find({ "title": { "$regex": title, "$options": "i" } }, { "_id": False, "title": True, "url": True })
    result = []
    for item in cursor:
        result.append((item["title"], item["url"]))
    return result



# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
