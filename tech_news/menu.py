import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def search(command):
    if command == 1:
        search_by_title(str(input("Digite o título: ")))
    elif command == 2:
        search_by_date(str(input("Digite a data no formato aaaa-mm-dd: ")))
    elif command == 3:
        search_by_source(str(input("Digite a fonte: ")))
    else:
        search_by_category(str(input("Digite a categoria: ")))


def get_top_news(command):
    if command == 5:
        top_5_news()
    else:
        top_5_categories()


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    print("Selecione uma das opções a seguir:")
    print(" 0 - Popular o banco com notícias;")
    print(" 1 - Buscar notícias por título;")
    print(" 2 - Buscar notícias por data;")
    print(" 3 - Buscar notícias por fonte;")
    print(" 4 - Buscar notícias por categoria;")
    print(" 5 - Listar top 5 notícias;")
    print(" 6 - Listar top 5 categorias;")
    print(" 7 - Sair.")
    try:
        user_entry = int(input())
        if 0 > user_entry or user_entry > 7:
            raise ValueError()
        if user_entry == 0:
            get_tech_news(
                int(input("Digite quantas notícias serão buscadas: "))
            )
        elif 0 < user_entry < 5:
            search(user_entry)
        elif 4 < user_entry < 7:
            get_top_news(user_entry)
        else:
            print("Encerrando script")
    except ValueError:
        sys.stderr.write("Opção inválida\n")
