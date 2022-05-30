import errors


def ask_dimensions():
    rows = 0
    columns = 0

    validation = False

    while not validation:
        rows = int(input('Ingrese el número de filas: '))
        rows_validation = errors.validate_rows_dimension(rows)

        if not rows_validation:
            continue

        columns = int(input('Ingrese el número de columnas: '))

        validation = errors.validate_boxes_dimension(rows, columns)

    return rows, columns


def print_interface_intro():
    print(f'\x1b[1;33m *' * 88)
    print("""
     ██ ██╗   ██ ███████╗ ██████╗  ██████╗     ███████ ███╗   ██╗ ██████ ██╗   ██ ███████ ███╗   ██ ████████ ██████╗  █████╗     ███████ ██╗   ██╗    ██████╗  █████╗ ██████╗ 
     ██ ██║   ██ ██╔════ ██╔════╝ ██╔═══██╗    ██╔════ ████╗  ██ ██╔════ ██║   ██ ██╔════ ████╗  ██ ╚══██╔══ ██╔══██ ██╔══██╗    ██╔════ ██║   ██║    ██╔══██ ██╔══██ ██╔══██╗
     ██ ██║   ██ █████╗  ██║  ███ ██║   ██║    █████╗  ██╔██╗ ██ ██║     ██║   ██ █████╗  ██╔██╗ ██║   ██║   ██████╔ ███████║    ███████ ██║   ██║    ██████╔ ███████ ██████╔╝
██   ██ ██║   ██ ██╔══╝  ██║   ██ ██║   ██║    ██╔══╝  ██║╚██╗██ ██║     ██║   ██ ██╔══╝  ██║╚██╗██║   ██║   ██╔══██ ██╔══██║    ╚════██ ██║   ██║    ██╔═══╝ ██╔══██ ██╔══██╗
╚█████╔ ╚██████╔ ███████╚ ██████╔╚ ██████╔╝    ███████ ██║ ╚████ ╚██████ ╚██████╔ ███████ ██║ ╚████║   ██║   ██║  ██ ██║  ██║    ███████ ╚██████╔╝    ██║     ██║  ██ ██║  ██║
 ╚════╝  ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝     ╚══════ ╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚══════ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝     ╚═╝     ╚═╝  ╚═ ╚═╝  ╚═╝                                                                                                                                                        
""")
    print(' *' * 88 + '\x1b[1;36m')
    print('Ingrese el número de filas y columnas del juego')
    print('El total de casilleros (filas x columnas) debe ser par! \n' + '\x1b[0;0m')
