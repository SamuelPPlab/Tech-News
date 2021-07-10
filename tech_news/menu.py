menu = """ Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair. """

menu_choice = [
    "Digite quantas notícias serão buscadas: ",
    "Digite o título: ",
    "Digite a data no formato aaaa-mm-dd: ",
    "Digite a fonte: ",
    "Digite a categoria: ",
    '',
    '',
    '',
    "Opção inválida",
]


# Requisito 12
def analyzer_menu():
    print(menu)


# Requisito 13
def menu_functions():
    continue_programe = True
    while continue_programe:
        analyzer_menu()
        choice = int(input())
        if choice < 0 or choice > 7:
            print(menu_choice[8])
        else:
            if choice != 7:
                value_informed = input(menu_choice[choice])
                print(value_informed)
        continue_programe = True if choice != 7 else False
