from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    found_news = search_news({"title": {"$regex": title, "$options": "i"}})

    news_list = []

    for news in found_news:
        title = news.get("title")
        url = news.get("url")

        news_list.append((title, url))

    return news_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    print(search_by_title("VAMOSCOMTUDO"))
