import random

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def create_table(rows, columns):
    table = []
    for row in range(rows):
        table.append([0] * columns)

    return table


def fill_table(table):
    n_rows = len(table)
    n_columns = len(table[0])
    n_boxes = n_rows * n_columns

    for i in range(n_boxes // 2):
        letter = random.choice(abc)

        i = 0

        while i < 2:
            random_row = random.randint(0, n_rows - 1)
            random_column = random.randint(0, n_columns - 1)

            box = table[random_row][random_column]

            if box == 0:
                table[random_row][random_column] = letter
                i += 1

        abc.remove(letter)

    return table


def print_table(table):
    n_rows = len(table)
    n_columns = len(table[0])

    print('\t\x1b[1;33m', end=' ')
    for i in range(1, n_columns + 1):
        print(f'\t{i}', end=' ')
    print()

    for i in range(n_rows):
        print(f'\t\x1b[1;33m{i + 1}', end=' ')

        for j in range(n_columns):
            box = table[i][j]
            print(f'\t\x1b[0;0m{box}', end=' ')

        print()
