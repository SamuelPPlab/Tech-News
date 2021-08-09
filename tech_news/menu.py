# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""

    print(
        "Selecione uma das opções a seguir:\n "
        "0 - Popular o banco com notícias;\n "
        "1 - Buscar notícias por título;\n "
        "2 - Buscar notícias por data;\n "
        "3 - Buscar notícias por fonte;\n "
        "4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n "
        "6 - Listar top 5 categorias;\n "
        "7 - Sair.\n"
    )
    option = input()
    if option == "0":
        print("Digite quantas notícias serão buscadas:")
    if option == "1":
        print("Digite o título")
    if option == "2":
        print("Digite a data no formato aaaa-mm-dd:")
    if option == "3":
        print("Digite a fonte:")
    if option == "4":
        print("Digite a categoria:")
