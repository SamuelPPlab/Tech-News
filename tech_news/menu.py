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


def get_by_news():
    amount = int(input("Digite quantas notícias serão buscadas:"))
    return get_tech_news(amount)


def get_by_title():
    amount = int(input("Digite o título:"))
    return search_by_title(amount)


def get_by_date():
    amount = int(input("Digite a data no formato aaaa-mm-dd:"))
    search_by_date(amount)


def get_by_source():
    amount = int(input("Digite a fonte:"))
    search_by_source(amount)


def get_by_category():
    amount = int(input("Digite a categoria:"))
    search_by_category(amount)


# Requisito 12
def analyzer_menu() -> None:  # Indica o retorno da func
    format = [
        " 0 - Popular o banco com notícias;",
        " 1 - Buscar notícias por título;",
        " 2 - Buscar notícias por data;",
        " 3 - Buscar notícias por fonte;",
        " 4 - Buscar notícias por categoria;",
        " 5 - Listar top 5 notícias;",
        " 6 - Listar top 5 categorias;",
        " 7 - Sair."
    ]
    print("Selecione uma das opções a seguir:")
    for item in format:
        print(item)
    try:
        user_response = int(input())
        if 0 <= user_response <= 7:
            raise_func = [
                get_by_news,
                get_by_title,
                get_by_date,
                get_by_source,
                get_by_category,
                top_5_news,
                top_5_categories,
            ]
            response = raise_func[user_response]()  # executa a função
            print(response)
    except ValueError:
        print("Opção inválida")
