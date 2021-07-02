from sys import stderr
from tech_news.scraper import get_tech_news
from tech_news.analyzer import search_engine as search, ratings


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    print(
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias;\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n 3 - Buscar notícias por fonte;\n 4 - Buscar notícias por categoria;\n 5 - Listar top 5 notícias;\n 6 - Listar top 5 categorias;\n 7 - Sair."
    )
    try:
        user_entry = int(input())
        if 0 > user_entry or user_entry > 7:
            raise ValueError()
        if user_entry == 0:
            get_tech_news(
                int(input("Digite quantas notícias serão buscadas: "))
            )
        elif user_entry == 1:
            search.search_by_title(str(input("Digite o título: ")))
        elif user_entry == 2:
            search.search_by_date(
                str(input("Digite a data no formato aaaa-mm-dd: "))
            )
        elif user_entry == 3:
            search.search_by_source(str(input("Digite a fonte: ")))
        elif user_entry == 4:
            search.search_by_category(str(input("Digite a categoria: ")))
        elif user_entry == 5:
            ratings.top_5_news()
        elif user_entry == 6:
            ratings.top_5_categories()
        else:
            print("Encerrando script")
    except ValueError:
        stderr.write("Opção inválida")
