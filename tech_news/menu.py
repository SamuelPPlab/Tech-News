from tech_news.menu_pack import menu_options
import sys

# Requisito 12


def analyzer_menu():
    print("Selecione uma das opções a seguir:")

    for index, option in enumerate(menu_options.options):
        print(f" {index} - {option[0]};")

    last_option = len(menu_options.options)
    print(f" {last_option} - Sair.")

    try:
        option_selected = int(input())

        if option_selected == last_option:
            print("Encerrando script")
            return
        result = menu_options.options[option_selected][1]()
        print(result)
    except ValueError:
        print("Opção inválida")

    except IndexError:
        print("Opção inválida", file=sys.stderr)
    except Exception as err:
        print(err)
