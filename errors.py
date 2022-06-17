# Definimos una función para validar que el número de filas de la tabla sea mayor a 1
def validate_rows_dimension(rows):
    if not 1 < rows:
        # Si el número de filas de la tabla no es mayor a 1, mostramos un mensaje de error
        print(format_error('El número de filas debe ser mayor a 1 \n'))
        return False
    return True


# Definimos una función para validar que la multiplicación entre el número de filas y columnas de la tabla,
# los casilleros, sea par y menor igual que 24
def validate_boxes_dimension(rows, columns):
    # Obtenemos el número de casilleros
    boxes = rows * columns

    # Validamos que sean menor o igual que 24 y par
    if not boxes <= 24 or not boxes % 2 == 0:
        print(format_error(f'El total de casilleros ({boxes}) debe ser par y menor que 25 \n'))
        return False
    return True


# Definimos una función para validar que el casillero que el usuario quiere abrir existe, no haya sido abierto o
# esté abierto
def validate_input_position(complete_table, input_row, input_column, opened_boxes,
                            actual_box_value):
    # Obtenemos las filas y columnas de la tabla en juego, para posteriormente validar si el casillero por abrir
    # se encuentra en ese rango
    n_rows = len(complete_table)
    n_columns = len(complete_table[0])

    # Definimos el casillero por abrir, para luego validar si ya ha sido abierto
    possible_box = (input_row - 1, input_column - 1)

    # Obtenemos la letra del casillero por abrir, para luego validar si se el casillero se encuentra actualmente abierto
    possible_box_value = None
    # Comprobamos que el casillero existe para poder obtener su valor
    if input_row <= n_rows and input_column <= n_columns:
        possible_box_value = complete_table[input_row - 1][input_column - 1]

    # Definimos el mensaje de error en blanco
    error_message = ''

    # Validamos si el casillero pertenece a la tabla
    if not input_row <= n_rows or not input_column <= n_columns:
        # Cambiamos el mensaje de error
        error_message = 'El casillero no existe, verifique la casilla que desea abrir!\n'
    # Validamos que el casillero no se encuentre abierto, viendo si hay algún casillero abierto y comparando su
    # valor con el que se intenta abrir y si este ya ha sido abierto
    elif actual_box_value is not None and actual_box_value == possible_box_value and possible_box in opened_boxes:
        # Cambiamos el mensaje de error
        error_message = 'Ese casillero está abierto actualmente\n'
    # Validamos si el casillero ha sido abierto
    elif possible_box in opened_boxes:
        # Cambiamos el mensaje de error
        error_message = 'Ese casillero ya fue abierto\n'
    else:
        return True

    # Imprimimos el mensaje de error con el formato correspondiente
    print(format_error(error_message))
    return False


# Definimos una función para dar formato a los mensajes de error, color rojo
def format_error(error):
    return '\x1b[1;31m' + error + '\x1b[0;0m'
