from tech_news.database import find_news
from functools import reduce


def top_5_news():
    news = find_news()
    searchResults = list()

    for item in news:
        rating = item["shares_count"] + item["comments_count"]
        searchResults.append((item["title"], item["url"], rating))

    searchResults.sort(key=lambda item: item[2], reverse=True)

    result = [(item[0], item[1]) for item in searchResults]
    return result[:5]


def top_5_categories():
    news = find_news()
    searchResults = [item["categories"] for item in news]

    formattedResults = reduce(lambda a, b: [*a, *b], searchResults, [])

    finalResults = list()

    for item in formattedResults:
        finalResults.append((item, formattedResults.count(item)))

    finalResults.sort(key=lambda item: item[0])
    finalResults.sort(key=lambda item: item[1], reverse=True)

    return [item[0] for item in finalResults][:5]
