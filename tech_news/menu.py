
import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import (top_5_news, top_5_categories)
from tech_news.analyzer.search_engine import (
    search_by_date,
    search_by_title,
    search_by_category,
    search_by_source
)


def zero():
    amount = int(input("Digite quantas notícias serão buscadas: "))
    get_tech_news(amount)


def one():
    title = input("Digite o título: ")
    print(search_by_title(title))


def two():
    date = input("Digite a data no formato aaaa-mm-dd: ")
    print(search_by_date(date))


def three():
    source = input("Digite a fonte: ")
    print(search_by_source(source))


def four():
    category = input("Digite a categoria: ")
    print(search_by_category(category))


def five():
    print(top_5_news())


def six():
    print(top_5_categories())


def seven():
    print("Encerrando script")


options = {
    0: zero,
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven
}


def action(option):
    options.get(option)()


# Requisito 12
def analyzer_menu():
    try:
        option = int(input(
            "Selecione uma das opções a seguir:\n "
            "0 - Popular o banco com notícias;\n "
            "1 - Buscar notícias por título;\n "
            "2 - Buscar notícias por data;\n "
            "3 - Buscar notícias por fonte;\n "
            "4 - Buscar notícias por categoria;\n "
            "5 - Listar top 5 notícias;\n "
            "6 - Listar top 5 categorias;\n "
            "7 - Sair.\n"
        ))

        action(option)

    except (TypeError, ValueError):
        sys.stderr.write("Opção inválida\n")
