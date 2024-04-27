# import os


def menu(options: list) -> None:
    # os.system("cls")
    menu_str = "\n" + "LISTA DE TAREAS DIARIAS".center(40) + "\n"

    for index, option in enumerate(options):
        menu_str += f"""
    [{index + 1}] => {option}"""
    menu_str += """

    [S] => Regresar o salir
    """
    print(menu_str)
