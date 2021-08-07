# Requisito 10
from tech_news.database import find_news
from functools import reduce


def top_5_news():
    """Seu código deve vir aqui"""
    info = list()
    news = find_news()
    for news_item in news:
        rate = news_item["shares_count"] + news_item["comments_count"]
        get_tuple = (news_item["title"], news_item["url"], rate)
        info.append(get_tuple)
    info.sort(key=lambda item: item[2], reverse=True)
    result = [(item[0], item[1]) for item in info]
    return result[:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    news = find_news()
    info = [news_item["categories"] for news_item in news]
    result = reduce(
        lambda news_list, current: [*news_list, *current], info, []
    )
    counter = list()
    for category in result:
        counter.append((category, result.count(category)))
    counter.sort(key=lambda item: item[0])
    counter.sort(key=lambda item: item[1], reverse=True)
    return [element[0] for element in counter][:5]
