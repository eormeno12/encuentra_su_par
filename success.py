# Definimos una función para imprimir que cierta letra ha sido encontrada
def letter_found(letter):
    print(format_success(f'{letter} HA SIDO ENCONTRADA!\n'))


# Definimos una función para decirle al usuario que ha ganado el juego
def win():
    print(format_success('FIN DEL JUEGO! GANASTE!\n'))


# Definimos una función para dar formato a los mensajes de éxito, color verde claro
def format_success(success):
    return '\x1b[1;32m' + success + '\x1b[0;0m'
