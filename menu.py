# Importamos el módulo de errores para poder validar las filas y columnas
import errors
import pandas as pd


# La función pide como parámetros la tabla con lo valores reales para poder validar posteiormente si el casillero fue
# abierto y pide opcionalmente el casillero actual, valor útil cuando el usuario ya reveló una letra y está
# buscando su par
def ask_box_position(complete_table, opened_boxes, actual_box_value=None):
    # Definimos la fila ingresada
    input_row = None

    # Definimos la columna ingresada
    input_column = None

    # Definimos la validación de la entrada
    validation = False

    # Mientras que el input no cumpla con la validación, se le pide al usuario que ingrese de nuevo los datos.
    while not validation:
        # Pedimos al usuario que ingrese la fila y columna con el formato fila,columna del casillero que desea abrir
        position = input('Abra un casillero en formato fila,columna (ej. 1,2) >>> ')

        # Obtenemos el primer valor del input, que es la fila
        input_row = int(position[0])

        # Obtenemos el tercer valor del input, que es la columna
        input_column = int(position[2])

        # Validamos que la fila y columna existan, que no esten abiertas o que no se encuentr abierta
        validation = errors.validate_input_position(complete_table, input_row, input_column, opened_boxes,
                                                    actual_box_value)

    return input_row - 1, input_column - 1


# Definimos una función para solicitar al usuario el número de filas y columnas de la tabla.
def ask_dimensions():
    # Definimos las filas para posteriormente solicitarlas al usuario
    rows = None

    # Definimos las columnas para posteriormente solicitarlas al usuario
    columns = None

    # Definimos el estado de la validación
    validated = False

    # Mientras que las filas y columnas se tengan que validar, se le solicita nuevamente al usuario que las ingrese
    while not validated:
        # Pedimos la usuario que ingrese el número de filas de la tabla
        rows = int(input('Ingrese el número de filas: '))

        # Validamos que el número de filas sea mayor a 1, mediante la función definida en el módulos de errors
        rows_validation = errors.validate_rows_dimension(rows)

        # Si el número de filas no es mayor a 1, volvemos a empezar el ciclo while
        if not rows_validation:
            continue

        # Pedimos la usuario que ingrese el número de columnas de la tabla
        columns = int(input('Ingrese el número de columnas: '))

        # Validamos que la multiplicación entre filas y columnas sea par y menor o igual que 24, usando la función
        # del módulo errors
        validated = errors.validate_boxes_dimension(rows, columns)

    return rows, columns


def print_interface_intro():
    # Imprimimos el nombre del juego con letras de color amarillo
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

    # Imprimimos las indicaciones del juego con letras de color cyan
    print('Ingrese el número de filas y columnas del juego')
    print('El total de casilleros (filas x columnas) debe ser par! \n' + '\x1b[0;0m')
