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


def zero():
    sub_option = input("Digite quantas notícias serão buscadas: ")
    print(get_tech_news(int(sub_option)))


def one():
    sub_option = input("Digite o título: ")
    print(search_by_title(sub_option))


def two():
    sub_option = input("Digite a data no formato aaaa-mm-dd: ")
    print(search_by_date(sub_option))


def three():
    sub_option = input("Digite a fonte: ")
    print(search_by_source(sub_option))


def four():
    sub_option = input("Digite a categoria: ")
    print(search_by_category(sub_option))


def five():
    print(top_5_news())


def six():
    print(top_5_categories())


def show_exit_message():
    print("Encerrando script")


COMMAND_OPTIONS = {
    "0": zero,
    "1": one,
    "2": two,
    "3": three,
    "4": four,
    "5": five,
    "6": six,
    "7": show_exit_message,
}


def show_menu():
    print(MENU_TITLE)
    for option in MENU_OPTIONS:
        print(option)


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    show_menu()
    option_chosed = input()
    if not option_chosed.isdigit() or int(option_chosed) not in range(8):
        print("Opção inválida", file=sys.stderr)
        return
    COMMAND_OPTIONS.get(option_chosed)()
