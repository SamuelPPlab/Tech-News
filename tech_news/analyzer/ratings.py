import tech_news.database as db
from tech_news.analyzer.search_engine_pack import search_engine_service

# Requisito 10


def top_5_news():
    news_list = db.find_news()
    news_list.sort(
        key=lambda news: news["comments_count"] + news["shares_count"],
        reverse=True,
    )

    return search_engine_service.get_tuple_list(news_list[:5])


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
