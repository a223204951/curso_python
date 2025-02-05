'''
tablero.py: Dibuja el tablero del juego del gato
'''
import random

def dibuja_tablero(simbolos: dict):
    '''
    Dibuja tablero del juego de el gato
    '''
    print(f'''
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ---------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ---------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
    ''')


def ia(simbolos: dict):
    """Estrategia de la computadora"""
    while True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ["X", "O"]:
            simbolos[x] = "O"
            break


def usuario(simbolos: dict):
    """Estrategia del usuario"""
    lista_numeros = [str(i) for i in range(1, 10)]  # del 1 al 9
    while True:
        x = input("Elija un número del 1 al 9: ")
        if x in lista_numeros and simbolos[x] not in ["X", "O"]:
            simbolos[x] = "X"
            break
        else:
            print("Entrada inválida o casilla ocupada. Intente de nuevo.")


def juego(simbolos: dict):
    """Juego del gato"""
    lista_combinaciones = [
        ["1", "2", "3"],  # Filas
        ["4", "5", "6"],
        ["7", "8", "9"],

        ["1", "4", "7"],  # Columnas
        ["2", "5", "8"],
        ["3", "6", "9"],

        ["1", "5", "9"],  # Diagonales
        ["3", "5", "7"]
    ]
    en_juego = True
    movimientos = 0
    dibuja_tablero(simbolos)

    while en_juego:
        usuario(simbolos)
        movimientos += 1
        dibuja_tablero(simbolos)
        gana = checa_winner(simbolos, lista_combinaciones)
        if gana is not None:
            break
        if movimientos == 9:
            return None

        ia(simbolos)
        movimientos += 1
        dibuja_tablero(simbolos)
        gana = checa_winner(simbolos, lista_combinaciones)
        if gana is not None:
            break
        if movimientos == 9:
            return None

    return gana


def checa_winner(simbolos: dict, combinaciones: list):
    """Checa si hay un ganador"""
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]] and simbolos[c[0]] in ["X", "O"]:
            return simbolos[c[0]]
    return None


if __name__ == '__main__':
    numeros = [str(i) for i in range(1, 10)]
    dsimbolos = {x: x for x in numeros}
    ganador = juego(dsimbolos)
    if ganador is None:
        print("Empate")
    else:
        print(f"El ganador es {ganador}")
