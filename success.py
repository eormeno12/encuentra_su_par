def letter_found(letter):
    print(format_success(f'{letter} HA SIDO ENCONTRADA!\n'))


def win():
    print(format_success('FIN DEL JUEGO! GANASTE!\n'))


def format_success(error):
    return '\x1b[1;32m' + error + '\x1b[0;0m'