from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.scraper import get_tech_news
import sys


def case0():
    total_noticias = input("Digite quantas notícias serão buscadas: ")
    return get_tech_news(total_noticias)


def case1():
    busca_titulo = input("Digite o título: ")
    return search_by_title(busca_titulo)


def case2():
    busca_data = input("Digite a data no formato aaaa-mm-dd: ")
    return search_by_date(busca_data)


def caso3():
    busca_fonte = input("Digite a fonte: ")
    return search_by_source(busca_fonte)


def caso4():
    busca_categoria = input("Digite a categoria: ")
    return search_by_category(busca_categoria)


def case5():
    return top_5_news()


def caso6():
    return top_5_categories()


def caso7():
    print("Encerrando script")


# Requisito 12
def analyzer_menu():
    escolhido = input(
        "Selecione uma das opções a seguir:\n"
        + " 0 - Popular o banco com notícias;\n"
        + " 1 - Buscar notícias por título;\n"
        + " 2 - Buscar notícias por data;\n"
        + " 3 - Buscar notícias por fonte;\n"
        + " 4 - Buscar notícias por categoria;\n"
        + " 5 - Listar top 5 notícias;\n"
        + " 6 - Listar top 5 categorias;\n"
        + " 7 - Sair.\n"
    )

    opcoes = {
        "0": case0,
        "1": case1,
        "2": case2,
        "3": caso3,
        "4": caso4,
        "5": case5,
        "6": caso6,
        "7": caso7,
    }

    try:
        result = opcoes[escolhido]()
        return result

    except Exception:
        return print("Opção inválida", file=sys.stderr)
