
import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def first_cases(option):
    if option == "0":
        print("Digite quantas notícias serão buscadas:")
        result = input()
        get_tech_news(result)
    elif option == "1":
        print("Digite o título:")
        title = input()
        result = search_by_title(title)
        print(result)
    elif option == "2":
        print("Digite a data no formato aaaa-mm-dd:")
        date = input()
        result = search_by_date(date)
        print(result)


def second_cases(option):
    if option == "3":
        print("Digite a fonte:")
        source = input()
        result = search_by_source(source)
        print(result)
    elif option == "4":
        print("Digite a categoria:")
        category = input()
        result = search_by_category(category)
        print(result)
    elif option == "5":
        result = top_5_news()
        print(result)


def last_cases(option):
    if option == "6":
        result = top_5_categories()
        print(result)
    elif option == "7":
        print("Encerrando script")


# Requisito 12
def analyzer_menu():
    print("Selecione uma das opções a seguir:")
    print(" 0 - Popular o banco com notícias;")
    print(" 1 - Buscar notícias por título;")
    print(" 2 - Buscar notícias por data;")
    print(" 3 - Buscar notícias por fonte;")
    print(" 4 - Buscar notícias por categoria;")
    print(" 5 - Listar top 5 notícias;")
    print(" 6 - Listar top 5 categorias;")
    print(" 7 - Sair.")

    option = input()

    if (option in ("0", "1", "2")):
        first_cases(option)
    elif (option in ("3", "4", "5")):
        second_cases(option)
    elif (option in ("6", "7")):
        last_cases(option)
    else:
        sys.stderr.write("Opção inválida\n")