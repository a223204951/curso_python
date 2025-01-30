# TABLERO.PY: DIBUJA EL
# TABLERO DEL JUEGO DEL
# GATO :3


import random

def dibuja_tablero(simbolos:dict):
    # DIBUJA EL TABLERO
    # DEL JUEGO DEL GATO
    print(f'''
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ---------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ---------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
    ''')

def ia(simbolos:dict):
    # ESTRETAGIA DE LA COMPUTADORA
    ocupado = True
    while ocupado is True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X', 'O']:
            simbolos[x] = 'O'
            ocupado = False

def usuario(simbolos:dict):
    # ESTRATEGIA DEL USUARIO
    ocupado = True
    lista_numeros = [str(i) for i in range(1, 10)]
    while ocupado is True:
        x = input('Elija un número del 1 al 9:   ')
        if x in lista_numeros:
            if simbolos[x] not in ['X', 'O']:
                simbolos[x] = 'X'
                ocupado = False
            else:
                print('Esta casilla ya está ocupada !!')

if __name__ == '__main__':
    numeros = [str(i) for i in range(1,10)]
    dsimbolos = {x:x for x in numeros}
    dibuja_tablero(dsimbolos)
    ia(dsimbolos)
    dibuja_tablero(dsimbolos)
    usuario(dsimbolos)
    dibuja_tablero(dsimbolos)