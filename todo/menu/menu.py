def menu(options: list, keys: list = ["f", "d", "b", "g", "e", "c", "a"]) -> None:
    key_used:list = []
    menu_str = "\n" + "LISTA DE TAREAS DIARIAS".center(40) + "\n"

    for key, option in zip(keys, options):
        key_used.append(key)
        menu_str += f"""
    [{key}] => {option}"""
    menu_str += """\n
    [s] => Regresar o salir
    """
    print(menu_str)
    return key_used
