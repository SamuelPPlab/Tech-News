import sys
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_source,
    search_by_category,
    search_by_date,
)
from tech_news.scraper import get_tech_news


def opcao_0():
    number = int(input("Digite quantas notícias serão buscadas:"))
    print(get_tech_news(number))


def opcao_1():
    title = input("Digite o título:")
    print(search_by_title(title))


def opcao_2():
    date = input("Digite a data no formato aaaa-mm-dd:")
    print(search_by_date(date))


def opcao_3():
    source = input("Digite a fonte:")
    print(search_by_source(source))


def opcao_4():
    number = input("Digite a categoria:")
    print(search_by_category(number))


def opcao_5():
    print(top_5_news())


def opcao_6():
    print(top_5_categories())


def opcao_7():
    print("Encerrando script")


# Requisito 12
def analyzer_menu():
    option = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
 """
    )

    responses = {
        "0": opcao_0,
        "1": opcao_1,
        "2": opcao_2,
        "3": opcao_3,
        "4": opcao_4,
        "5": opcao_5,
        "6": opcao_6,
        "7": opcao_7,
    }
    if option != "" and 0 <= int(option) <= 7:
        responses[option]()
    else:
        print("Opção inválida", file=sys.stderr)


# analyzer_menu()
