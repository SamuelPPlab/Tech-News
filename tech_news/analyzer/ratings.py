# Requisito 10
from tech_news.database import find_news

# https://pythonhelp.wordpress.com/2014/04/06/ordenacao-de-uma-lista/


def top_5_news():
    for index, valor in enumerate(
        [
            item
            for item in find_news()
            if (item["shares_count"] + item["comments_count"])
        ].sort(reverse=True)
    ):
        if index < 5:
            return (f"noticia_{index + 1}", valor["url"])


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
