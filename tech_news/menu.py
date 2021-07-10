from scraper import get_tech_news
from analyzer.search_engine import search_by_title, search_by_date
from analyzer.search_engine import search_by_source, search_by_category
from analyzer.ratings import top_5_news, top_5_categories


menu = """ Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair. """

menu_choice = [
    "Digite quantas notícias serão buscadas: ",
    "Digite o título: ",
    "Digite a data no formato aaaa-mm-dd: ",
    "Digite a fonte: ",
    "Digite a categoria: ",
    '',
    '',
    '',
    "Opção inválida",
]


# Requisito 12
def analyzer_menu():
    print(menu)


def menu_functions_auxiliar(n):
    if n != 7:
        value_informed = input(menu_choice[n])
    if n == 0:
        get_tech_news(int(value_informed))
    elif n == 1:
        print(search_by_title(value_informed))
    elif n == 2:
        print(search_by_date(value_informed))
    elif n == 3:
        print(search_by_source(value_informed))
    elif n == 4:
        print(search_by_category(value_informed))
    elif n == 5:
        print(top_5_news())
    elif n == 6:
        print(top_5_categories())


# Requisito 13
def menu_functions():
    continue_programe = True
    while continue_programe:
        analyzer_menu()
        choice = int(input())
        if choice < 0 or choice > 7:
            print(menu_choice[8])
        else:
            menu_functions_auxiliar(choice)
        continue_programe = True if choice != 7 else False
