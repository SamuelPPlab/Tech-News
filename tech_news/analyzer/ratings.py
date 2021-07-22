from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """
        - Pesquisa no DB e retorna as 5 notícias mais populares;
            - Calcula popularidade pela soma de compartilhamentos e comentários
            - Ordena resultados alfabeticamente por título;
            - Havendo menos de 5 notícias, retorna quantas tiver
    """
    get_all_news = find_news()
    news_info = [
       (
           news["title"], news["url"],
           news["shares_count"] + news["comments_count"]
        )
       for news in get_all_news
    ]
    sorted(news_info, key=lambda news: news[0], reverse=True)

    news_by_popularity = [
        (info[0], info[1]) for info in news_info
    ]
    return news_by_popularity[:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
