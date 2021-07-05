from tech_news.database import search_news
from tech_news.analyzer.search_engine import format_document

# Requisito 10
def top_5_news():
    results = search_news({})
    results.sort(key=lambda news: news["shares_count"] + news["comments_count"], reverse=True)
    return [format_document(news) for news in results[:5]]


# Requisito 11
def top_5_categories():
    categories = {}
    results = search_news({})

    for result in results:
        for category in result["categories"]:
            categories[category] = 0
    
    for result in results:
        for category in result["categories"]:
            categories[category] += 1
    
    categories_list = sorted(categories.items(), key=lambda category: category[0])
    categories_list.sort(key=lambda category: category[1], reverse=True)
    return [category[0] for category in categories_list[:5]]
