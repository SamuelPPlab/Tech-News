from tech_news.database import find_news
from tech_news.analyzer.search_engine import format_result


# Requisito 10
def top_5_news():
    return format_result(
        sorted(
            find_news(),
            key=lambda field: (
                -(field["shares_count"] + field["comments_count"]),
                field["title"],
            ),
        )[:5]
    )


# Requisito 11
def top_5_categories():
    categories_frequency = {}
    for news in find_news():
        for category in news["categories"]:
            if category in categories_frequency:
                categories_frequency[category] += 1
            else:
                categories_frequency[category] = 1
    categories_sorted_by_ranking = [
        item[0]
        for item in sorted(
            categories_frequency.items(), key=lambda k: (-k[1], k[0])
        )
    ]
    top_five_categories = categories_sorted_by_ranking[:5]
    return sorted(top_five_categories)
