import menu
import table
import errors
import success

opened_boxes = []


def ask_box_position(complete_table, actual_box_value=None):
    input_row = None
    input_column = None

    validation = False
    while not validation:
        position = input('Abra un casillero en formato fila,columna (ej. 1,2) >>> ')
        input_row = int(position[0])
        input_column = int(position[2])

        validation = errors.validate_input_position(complete_table, input_row, input_column, opened_boxes,
                                                    actual_box_value)

    return input_row - 1, input_column - 1


def run():
    menu.print_interface_intro()
    n_rows, n_columns = menu.ask_dimensions()

    base_table = table.create_table(n_rows, n_columns)
    hidden_table = table.create_table(n_rows, n_columns, '*')

    complete_table = table.fill_table(base_table)

    table.print_table(hidden_table)

    while hidden_table != complete_table:
        input_row, input_column = ask_box_position(complete_table)
        table.show_element_table(hidden_table, complete_table, input_row, input_column)
        opened_boxes.append((input_row, input_column))

        actual_box = (input_row, input_column)
        pair_found = False

        while not pair_found:
            actual_box_value = complete_table[actual_box[0]][actual_box[1]]

            input_row, input_column = ask_box_position(complete_table, actual_box_value)

            possible_box = (input_row, input_column)
            possible_box_value = complete_table[possible_box[0]][possible_box[1]]

            if actual_box_value == possible_box_value and actual_box != possible_box:
                table.show_element_table(hidden_table, complete_table, input_row, input_column)

                letter = actual_box_value
                pair_found = True
                opened_boxes.append((input_row, input_column))

                success.letter_found(letter)
            else:
                table.print_table(hidden_table)

    success.win()


if __name__ == '__main__':
    run()
