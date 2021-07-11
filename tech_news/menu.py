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


# Requisito 12
def analyzer_menu():
    menu_questions = (
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )
    response = input(menu_questions)
    result = "Opção inválida"
    if response == "0":
        result = input("Digite quantas notícias serão buscadas:")
        get_tech_news(int(result))
    elif response == "1":
        result = input("Digite o título:")
        print(search_by_title(result))
    elif response == "2":
        result = input("Digite a data no formato aaaa-mm-dd:")
        print(search_by_date(result))
    elif response == "3":
        result = input("Digite a fonte:")
        print(search_by_source(result))
    elif response == "4":
        result = input("Digite a categoria:")
        print(search_by_category(result))
    elif response == "5":
        print(top_5_news())
    elif response == "6":
        print(top_5_categories())
    elif response == "7":
        print("Encerrando script")
        return
    else:
        print(result, file=sys.stderr)
        return result


# analyzer_menu()
