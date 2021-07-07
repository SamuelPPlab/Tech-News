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

SUBMENU_OPTIONS = [
    "Digite quantas notícias serão buscadas:",
    "Digite o título:",
    "Digite a data no formato aaaa-mm-dd:",
    "Digite a fonte:",
    "Digite a categoria:",
]


def show_exit_message():
    print("Encerrando script")


COMMAND_OPTIONS = [
    get_tech_news,
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
    top_5_news,
    top_5_categories,
    show_exit_message,
]


def show_menu():
    print("Selecione uma das opções a seguir:")
    for option in MENU_OPTIONS:
        print(option)


def analyzer_menu():
    show_menu()
    try:
        chosen_number = int(input())
        if 0 <= chosen_number < len(MENU_OPTIONS):
            if 0 <= chosen_number < len(SUBMENU_OPTIONS):
                chosen_term = input(SUBMENU_OPTIONS[chosen_number])
                COMMAND_OPTIONS[chosen_number](chosen_term)
            else:
                COMMAND_OPTIONS[chosen_number]()
        else:
            raise ValueError()
    except Exception:
        sys.stderr.write("Opção inválida\n")
