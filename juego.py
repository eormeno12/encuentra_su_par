# Importamos los módulos correspondientes
import menu
import table
import success
import database.database as db

# Definimos la lista de casilleros abiertos
opened_boxes = []


# Función donde se define la lógica del juego
def run():
    # Se imprime la intro de la interface del juego Encuentra su Par
    menu.print_interface_intro()

    # Pedidos al usuario las dimensiones de la tabla a jugar
    n_rows, n_columns = menu.ask_dimensions()

    # Creamos la tabla base para la tabla con letras aleatorias
    base_table = table.create_table(n_rows, n_columns)

    # Creamos la tabla con *, para que el usuario no conozca los valores reales
    hidden_table = table.create_table(n_rows, n_columns, '*')

    # Llenamos la tabla base con letras aleatorias
    complete_table = table.fill_table(base_table)

    # Imprimimos la tabla con los valores ocultos (*)
    table.print_table(hidden_table)

    db.create_file()

    # Mientras que la tabla con la que juega el usuario no sea igual a aquella con los valores reales,
    # se sigue jugando porque significa que todavia no gana
    while hidden_table != complete_table:
        database = db.read_file()

        # Pedimos al usuario que ingrese la fila y columna del casillero a abrir
        input_row, input_column = menu.ask_box_position(complete_table, opened_boxes)

        # Mostramos al usuario la taba con los valores ocultos, revelando la letra del casillero que elegió
        table.show_element_table(hidden_table, complete_table, input_row, input_column)

        # Agregamos la fila y columna a la lista de casilleros abiertos, aquel que el usuario acaba de revelar
        opened_boxes.append((input_row, input_column))

        # Definimos el casillero en el que se encuentra el usuario, el casillero que acaba de abrir
        actual_box = (input_row, input_column)

        # Obtenemos la letra del casillero abierto
        actual_box_value = complete_table[actual_box[0]][actual_box[1]]

        # Definimos si el par de la letra se ha encontrado
        pair_found = False

        letter_dict = db.letter_json_format(actual_box_value, actual_box)
        db.add_letter(database, letter_dict)
        db.update_file(database)


        # Mientras que el par de la letra no se encuentre, le seguiremos pidiendo al usuario que ingrese otra
        # posición de fila y columna para abrir
        attempts_count = 0
        while not pair_found:
            attempts_count += 1

            # Pedimos al usuario que ingrese la fila y columna del casillero a abrir, y así comprobar si ha
            # encontrado al par de la letra
            input_row, input_column = menu.ask_box_position(complete_table, opened_boxes, actual_box_value)

            # Definimos el casillero que acaba de abrir el usuario, donde podría encontrarse el par de la letra
            possible_box = (input_row, input_column)

            # Obtenemos la letra del casillero
            possible_box_value = complete_table[possible_box[0]][possible_box[1]]

            # Validamos si las letras son iguales y que la fila  columna de los casilleros son diferentes,
            # para así saber si el usuario encontro el par de la letra
            if actual_box_value == possible_box_value and actual_box != possible_box:
                # Si el usuario encontro el par de la letra, la revelamos en la tabla
                table.show_element_table(hidden_table, complete_table, input_row, input_column)

                # Definimos una variable con la letra econtrada
                letter = actual_box_value

                # Declaramos que la letra fue encontrade, para terminar el ciclo while
                pair_found = True

                # Agregamos la fila y columna a la lista de casilleros abiertos
                opened_boxes.append((input_row, input_column))

                # Imprimimos un mensaje de que la letra fue encontrada exitosamente
                success.letter_found(letter)
            else:
                # Si el usuario no encontro el par, volvemos a imprimir la tabla
                table.show_element_table(hidden_table, complete_table, input_row, input_column)
                hidden_table[input_row][input_column] = '*'

            attempt_dict = db.attempt_json_format(attempts_count, possible_box, pair_found)
            db.add_attempt(database, actual_box_value, attempt_dict)
            db.update_file(database)

    # Cuando termina el ciclo while, significa que el usuario ganó, por lo que imprimimos un mensaje de éxito
    success.win()
    game_summary = db.update_history(n_rows, n_columns)
    db.print_game_summary(game_summary)


if __name__ == '__main__':
    run()
