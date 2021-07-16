
dic_option_input = {
    0: "Digite quantas notícias serão buscadas:",
    1: "Digite o título:",
    2: "Digite a data no formato aaaa-mm-dd:",
    3: "Digite a fonte:",
    4: "Digite a categoria: ",
    5: "",
    6: "",
    7: ""
}


# Requisito 12
def analyzer_menu():
    try:
        print(
            "Selecione uma das opções a seguir:\n" +
            "0 - Popular o banco com notícias;\n" +
            "1 - Buscar notícias por título;\n" +
            "2 - Buscar notícias por data;\n" +
            "3 - Buscar notícias por fonte;\n" +
            "4 - Buscar notícias por categoria;\n" +
            "5 - Listar top 5 notícias;\n" +
            "6 - Listar top 5 categorias;\n" +
            "7 - Sair."
        )

        option = int(input())
        if(option < 0 or option > 7):
            print("Opção inválida\n")
        else:
            print(dic_option_input[option])
    except ValueError:
        print("Opção inválida\n")
