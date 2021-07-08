from tech_news.database import find_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    ordered = sorted(find_news(), key=itemgetter("title"))
    top = sorted(
        ordered,
        key=lambda item: item["shares_count"] + item["comments_count"],
        reverse=True,
    )[:5]
    return [(top["title"], top["url"]) for top in top]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
