from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    news_found = search_news({"title": {"$regex": title, "$options": "i"}})

    news_list = []

    for news in news_found:
        title = news.get("title")
        url = news.get("url")

        news_list.append((title, url))

    return news_list


# Requisito 7
def search_by_date(date):
    try:
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:])

        date = datetime.datetime(year=year, month=month, day=day)
        date = f"{date.date()}"
    except ValueError:
        raise ValueError("Data inválida")

    news_found = search_news({"timestamp": {"$regex": date}})

    news_list = []

    for news in news_found:
        title = news.get("title")
        url = news.get("url")

        news_list.append((title, url))

    return news_list


# Requisito 8
def search_by_source(source):
    news_found = search_news({"sources": {"$regex": source, "$options": "i"}})

    news_list = []

    for news in news_found:
        title = news.get("title")
        url = news.get("url")

        news_list.append((title, url))

    return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    print(search_by_source("ResetEra"))
