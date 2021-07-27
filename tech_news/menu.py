import sys

# Requisito 12
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
  search_by_category,
  search_by_date,
  search_by_source,
  search_by_title
)


def populate_database():
    amount = input("Digite quantas notícias serão buscadas:")
    get_tech_news(int(amount))


def find_by_title():
    title = input("Digite o título:")
    search_by_title(title)


def find_by_date():
    date = input("Digite a data no formato aaaa-mm-dd:")
    search_by_date(date)


def find_by_source():
    source = input("Digite a fonte:")
    search_by_source(source)


def find_by_category():
    category = input("Digite a categoria:")
    search_by_category(category)


def get_top_5_news():
    top_5_news()


def get_top_5_categories():
    top_5_categories()


def end_script():
    print('Encerrando script')


actions = {
  0: populate_database,
  1: find_by_title,
  2: find_by_date,
  3: find_by_source,
  4: find_by_category,
  5: get_top_5_news,
  6: get_top_5_categories,
  7: end_script
}


def analyzer_menu():
    option = input("""Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.""")
    if (option != "" and 0 <= int(option) <= 7):
        return actions[int(option)]()
    else:
        print("Opção inválida", file=sys.stderr)
