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


def validate_input_position(complete_table, input_row, input_column, opened_boxes,
                            actual_box_value):
    n_rows = len(complete_table)
    n_columns = len(complete_table[0])

    possible_box = (input_row - 1, input_column - 1)
    possible_box_value = complete_table[input_row - 1][input_column - 1]

    error_message = ''

    if not input_row <= n_rows or not input_column <= n_columns:
        error_message = 'El casillero no existe, verifique la casilla que desea abrir!\n'
    elif actual_box_value is not None and actual_box_value == possible_box_value and possible_box in opened_boxes:
        error_message = 'Ese casillero está abierto actualmente\n'
    elif possible_box in opened_boxes:
        error_message = 'Ese casillero ya fue abierto\n'
    else:
        return True

    print(format_error(error_message))
    return False


def format_error(error):
    return '\x1b[1;31m' + error + '\x1b[0;0m'
