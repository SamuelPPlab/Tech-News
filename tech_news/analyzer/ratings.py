from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    news = find_news()

    for new in news:
        new["popularity"] = new["comments_count"] + new["shares_count"]

    classify_news = sorted(news, key=lambda n: n["popularity"], reverse=True)
    five_selected_news = [new for new in classify_news[:5]]
    top_news_five = [(new["title"], new["url"]) for new in five_selected_news]

    return top_news_five


# Requisito 11
def top_5_categories():
    news = find_news()

    categories_news = []
    sorted_categories = []

    for news in news:
        for category in news['categories']:
            categories_news.append(category)

    quantity_categories = sorted(Counter(categories_news).most_common())

    for category_and_qty in quantity_categories:
        sorted_categories.append(category_and_qty[0])

    return sorted_categories[:5]
