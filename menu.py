def ask_dimensions():
    rows = 0
    columns = 0

    validation = False

    while not validation:
        rows = int(input('Ingrese el número de filas: '))
        rows_validation = validate_rows_dimension(rows)

        if not rows_validation:
            continue

        columns = int(input('Ingrese el número de columnas: '))

        boxes_validation = validate_boxes_dimension(rows, columns)

        if not boxes_validation:
            continue

        validation = True

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


def validate_rows_dimension(rows):
    if not 1 < rows:
        print(format_error('El número de filas debe ser mayor a 1 \n'))
        return False

    return True


def validate_boxes_dimension(rows, columns):
    boxes = rows * columns
    if not boxes <= 24 or not boxes % 2 == 0:
        print(format_error(f'El total de casilleros ({boxes}) debe ser par y menor que 25 \n'))
        return False
    return True


def format_error(error):
    return '\x1b[1;31m' + error + '\x1b[0;0m'
