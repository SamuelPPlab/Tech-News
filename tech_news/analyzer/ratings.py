from operator import itemgetter
from tech_news.database import find_news
from tech_news.analyzer.search_engine import filter_title_url


def order_by_shares_plus_comments_and_name(array):
    order_by_name = sorted(array, key=itemgetter("title"))
    return sorted(
        order_by_name,
        key=lambda item: item["shares_count"] + item["comments_count"],
        reverse=True,
    )


def top_news():
    return order_by_shares_plus_comments_and_name(find_news())[:5]


def get_categories(dict):
    return dict["categories"]


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news = top_news()
    return [filter_title_url(news) for news in news]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    categories = []
    for item in top_news():
        categories.extend(get_categories(item))
    categories.sort()
    return categories[:5]
