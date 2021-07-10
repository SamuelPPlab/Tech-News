def insert_database_opt():
    input("Digite quantas notícias serão buscadas:")


def search_by_title_opt():
    input("Digite o título:")


def search_by_date_opt():
    input("Digite a data no formato aaaa-mm-dd:")


def search_by_source_opt():
    input("Digite a fonte:")


def search_by_category_opt():
    input("Digite a categoria:")


def search_top5_news_opt():
    print("Não codei isso ainda")


def search_top5_category_opt():
    print("Não codei isso ainda")


# Requisito 12
def analyzer_menu():
    options = [
        ("Popular o banco com notícias", insert_database_opt),
        ("Buscar notícias por título", search_by_title_opt),
        ("Buscar notícias por data", search_by_date_opt),
        ("Buscar notícias por fonte", search_by_source_opt),
        ("Buscar notícias por categoria", search_by_category_opt),
        ("Listar top 5 notícias", search_top5_news_opt),
        ("Listar top 5 categorias", search_top5_category_opt),
    ]
    print("Selecione uma das opções a seguir:")
    for index, option in enumerate(options):
        print(f" {index} - {option[0]};")

    option_selected = input(f" {len(options)} - Sair.\n")

    try:
        options[int(option_selected)][1]()
    except ValueError:
        print("Opção inválida")
