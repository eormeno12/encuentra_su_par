# Importamos la librería random para luego usarla con las selección aleatoria de letras y casilleros
import random

# Definimos una lista con las letras
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z']


# Definimos una función que crea una tabla según el número de filas y columnas que se le brinda. Además, cuenta con
# un parámetro char opcional, que es útil cuando queremos crear la tabla inicial con la que jugará el usuario
def create_table(rows, columns, char=0):
    table = []
    for row in range(rows):
        table.append([char] * columns)

    return table


# Definimos una función para llenar la tabla con las letras
def fill_table(table):
    n_rows = len(table)
    n_columns = len(table[0])
    n_boxes = n_rows * n_columns

    # Recorremos la tabla en un rango de la mitad de sus casilleros, ya que debemos colocar una letra en dos casilleros
    for i in range(n_boxes // 2):
        # Escogemos una letra aleatoria
        letter = random.choice(abc)

        i = 0

        # Creamos un ciclo while que buscará dos casilleros aleatorios donde colocar la letra seleccionada
        while i < 2:
            # Escohemos una fila y columna aleatoria
            random_row = random.randint(0, n_rows - 1)
            random_column = random.randint(0, n_columns - 1)

            # Obtenemos el valor en esa fila y columna
            box = table[random_row][random_column]

            # Si el valor es igual a 0, valor con el que se crea la tabla base, entonces podemos cambiarlo por la letra,
            # porque significa que no ha sido modificado previamente
            if box == 0:
                table[random_row][random_column] = letter
                i += 1

        # Una vez agregamos la letra, la quitamos de la lista para no repetirla
        abc.remove(letter)

    return table


# Definimos una función para imprimir la tabla
def print_table(table):
    n_rows = len(table)
    n_columns = len(table[0])

    # Le damos espacio a la tabla y cambiamos el color a amarillo
    print('\t\x1b[1;33m', end=' ')

    # Imprimimos los número de las columnas con espacio
    for i in range(1, n_columns + 1):
        print(f'\t{i}', end=' ')
    print()

    # Iteramos para imprimir las filas
    for i in range(n_rows):
        # Imprimimos el número de la fila con color amarillo
        print(f'\t\x1b[1;33m{i + 1}', end=' ')

        # Iteramos para imprimir los valores en esa fila
        for j in range(n_columns):
            # Obtenemos el valor
            box = table[i][j]

            # Si el valor ha sido revelado, la letra ha sido encontrada, lo imprimimos con color cyan
            if box != '*':
                print(f'\t\x1b[1;36m{box}', end=' ')
            # Sino lo imprimimos en color blanco
            else:
                print(f'\t\x1b[0;0m{box}', end=' ')

        print('\x1b[0;0m')


# Definimos una función para una letra en la tabla
def show_element_table(hidden_table, table, row, column):
    # Cambiamos el valor oculto por la letra correspondiente, en la fila y columna pedida como parámetro
    hidden_table[row][column] = table[row][column]

    # Imprimimos la nueva tabla
    print_table(hidden_table)
