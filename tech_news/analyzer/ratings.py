# Requisito 10
from tech_news.database import find_news
from operator import itemgetter


# https://www.programiz.com/python-programming/methods/built-in/sorted
# https://stackoverflow.com/questions/18595686/how-do-operator-itemgetter-and-sort-work
def top_5_news():
    order_by_name = sorted(find_news(), key=itemgetter("title"))   
    top = sorted(
        order_by_name,
        key=lambda item: item["shares_count"] + item["comments_count"],
        reverse=True,
    )[:5]
    return [(top["title"], top["url"]) for top in top]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
