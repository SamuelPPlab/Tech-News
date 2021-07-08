from analyzer.ratings import top_5_news, top_5_categories
from analyzer.search_engine import search_by_title, search_by_date
from analyzer.search_engine import search_by_source, search_by_category
from scraper import get_tech_news


def opcao_0():
    number = input("Digite quantas notícias serão buscadas:")
    get_tech_news(number)


def opcao_1():
    number = input("Digite o título:")
    search_by_title(number)


def opcao_2():
    number = input("Digite a data no formato aaaa-mm-dd:")
    search_by_date(number)


def opcao_3():
    number = input("Digite a fonte:")
    search_by_source(number)


def opcao_4():
    number = input("Digite a categoria:")
    search_by_category(number)


def opcao_5():
    top_5_news()


def opcao_6():
    top_5_categories()


def opcao_7():
    print('SAIR')


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    option = input("""Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
 """)

    responses = [
        opcao_0, opcao_1, opcao_2, opcao_3, opcao_4, opcao_5, opcao_6, opcao_7]
    if 0 <= option <= 7:
        responses[option]()
    else:
        raise Exception("Opção inválida")  # isso mesmo?


analyzer_menu()
