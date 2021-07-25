from tech_news.database import find_news


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
    """Seu código deve vir aqui"""
