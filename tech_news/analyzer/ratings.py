# Requisito 10
from tech_news.database import find_news


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
