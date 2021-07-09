# Requisito 12
import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import (
    top_5_news,
    top_5_categories,
)

MENU_TITLE = "Selecione uma das opções a seguir:"
MENU_OPTIONS = [
    " 0 - Popular o banco com notícias;",
    " 1 - Buscar notícias por título;",
    " 2 - Buscar notícias por data;",
    " 3 - Buscar notícias por fonte;",
    " 4 - Buscar notícias por categoria;",
    " 5 - Listar top 5 notícias;",
    " 6 - Listar top 5 categorias;",
    " 7 - Sair.",
]


def option_zero():
    sub_option = input("Digite quantas notícias serão buscadas: ")
    print(get_tech_news(int(sub_option)))


def option_one():
    sub_option = input("Digite o título: ")
    print(search_by_title(sub_option))


def option_two():
    sub_option = input("Digite a data no formato aaaa-mm-dd: ")
    print(search_by_date(sub_option))


def option_three():
    sub_option = input("Digite a fonte: ")
    print(search_by_source(sub_option))


def option_four():
    sub_option = input("Digite a categoria: ")
    print(search_by_category(sub_option))


def option_five():
    print(top_5_news())


def option_six():
    print(top_5_categories())


def show_exit_message():
    print("Encerrando script")


COMMAND_OPTIONS = {
    "0": option_zero,
    "1": option_one,
    "2": option_two,
    "3": option_three,
    "4": option_four,
    "5": option_five,
    "6": option_six,
    "7": show_exit_message,
}


def show_menu():
    print("Selecione uma das opções a seguir:")
    for option in MENU_OPTIONS:
        print(option)


def analyzer_menu():
    show_menu()
    chosen_number = input()
    if not chosen_number.isdigit() or int(chosen_number) not in range(8):
        print("Opção inválida", file=sys.stderr)
        return
    COMMAND_OPTIONS.get(chosen_number)()
