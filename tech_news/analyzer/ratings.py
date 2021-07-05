from tech_news.database import search_news
from tech_news.analyzer.search_engine import format_document

# Requisito 10
def top_5_news():
    results = search_news({})
    results.sort(key=lambda news: news["shares_count"] + news["comments_count"], reverse=True)
    return [format_document(news) for news in results[:5]]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
