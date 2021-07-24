from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category
)
from tech_news.analyzer.ratings import (
    top_5_news,
    top_5_categories
)


def zero():
    entryData = input("Digite quantas notícias serão buscadas: ")
    print(get_tech_news(int(entryData)))


def one():
    entryData = input("Digite o título: ")
    print(search_by_title(entryData))


def two():
    entryData = input("Digite a data no formato aaaa-mm-dd: ")
    print(search_by_date(entryData))


def three():
    entryData = input("Digite a fonte: ")
    print(search_by_source(entryData))


def four():
    entryData = input("Digite a categoria: ")
    print(search_by_category(entryData))


def five():
    print(top_5_news())


def six():
    print(top_5_categories())


def exit():
    print("Vlw flw!")


# Requisito 12
def analyzer_menu():
    MENU = [
        " 0 - Popular o banco com notícias;",
        " 1 - Buscar notícias por título;",
        " 2 - Buscar notícias por data;",
        " 3 - Buscar notícias por fonte;",
        " 4 - Buscar notícias por categoria;",
        " 5 - Listar top 5 notícias;",
        " 6 - Listar top 5 categorias;",
        " 7 - Sair.",
    ]

    OPTIONS = {
        "0": zero,
        "1": one,
        "2": two,
        "3": three,
        "4": four,
        "5": five,
        "6": six,
        "7": exit,
    }

    print("Selecione uma das opções a seguir:")
    for item in MENU:
        print(item)
    try:
        response = int(input())
        if 0 <= response <= 7:
            response = OPTIONS[response]()
    except ValueError:
        print("Opção inválida")
