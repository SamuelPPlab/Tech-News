from tech_news.database import search_news, find_news
import datetime


def title_and_url(all_news):
    title_and_url_news = []
    for news in all_news:
        title_and_url_news.append((news["title"], news["url"]))
    return title_and_url_news


# Requisito 6
def search_by_title(title):
    all_news = search_news(
        {"title": {"$regex": f"{title}", "$options": "i"}}
    )  # query @rafaelmguimaraes

    title_and_url_news = title_and_url(all_news)
    return title_and_url_news


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        all_news = search_news(
            {"timestamp": {"$regex": f"{date}", "$options": "i"}}
        )
        title_and_url_news = title_and_url(all_news)
        return title_and_url_news

    except ValueError:
        raise ValueError("Data inválida")


def search_in_list_category(search, category):
    all_news = find_news()
    selected_news = []

    for news in all_news:
        if search.lower() in map(
            str.lower, news[category]
        ):  # código @andersonmalves
            selected_news.append((news["title"], news["url"]))
    return selected_news


# Requisito 8
def search_by_source(source):
    return search_in_list_category(source, "sources")


# Requisito 9
def search_by_category(category):
    return search_in_list_category(category, "categories")
