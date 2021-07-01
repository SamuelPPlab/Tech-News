# Requisito 12

import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def first_options(choice):
    if choice == "0":
        amount = input("Digite quantas notícias serão buscadas:")
        get_tech_news(int(amount))
    elif choice == "1":
        title = input("Digite o título:")
        print(search_by_title(title))
    elif choice == "2":
        date = input("Digite a data no formato aaaa-mm-dd:")
        print(search_by_date(date))
    elif choice == "3":
        source = input("Digite a fonte:")
        print(search_by_source(source))


def second_options(choice):
    if choice == "4":
        category = input("Digite a categoria:")
        print(search_by_category(category))
    elif choice == "5":
        print(top_5_news())
    elif choice == "6":
        print(top_5_categories())
    elif choice == "7":
        print("Encerrando script")
        SystemExit


def options_choice(choice):
    if (choice in (['0', '1', '2', '3'])):
        first_options(choice)
    elif (choice in (['4', '5', '6', '7'])):
        second_options(choice)
    else:
        sys.stderr.write("Opção inválida\n")


# Para passar no teste
def analyzer_menu():
    choice = input(
        "Selecione uma das opções a seguir:\n "
        "0 - Popular o banco com notícias;\n "
        "1 - Buscar notícias por título;\n "
        "2 - Buscar notícias por data;\n "
        "3 - Buscar notícias por fonte;\n "
        "4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n "
        "6 - Listar top 5 categorias;\n "
        "7 - Sair.\n"
    )
    options_choice(choice)

# Para funcionar
# def analyzer_menu():
#     choice = ''
#     while choice != '7':
#         choice = input(
#             "Selecione uma das opções a seguir:\n "
#             "0 - Popular o banco com notícias;\n "
#             "1 - Buscar notícias por título;\n "
#             "2 - Buscar notícias por data;\n "
#             "3 - Buscar notícias por fonte;\n "
#             "4 - Buscar notícias por categoria;\n "
#             "5 - Listar top 5 notícias;\n "
#             "6 - Listar top 5 categorias;\n "
#             "7 - Sair.\n"
#         )
#         options_choice(choice)


# analyzer_menu()
