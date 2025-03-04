'''Este archivo es el punto de entrada a la aplicacion. Aqui se importan las funciones de tablero.py y se ejecutan en un ciclo while.'''
 
import tablero
 
def main():
    ''' Punto de entrada a la aplicacion '''
    X = {"G":0,"P":0,"E":0}
    O = {"G":0,"P":0,"E":0}
    score = {"X":X,"O":O}
    numeros = {str(i):str(i) for i in range(1,10)}
    corriendo = True
    while corriendo:
        dsimbolos = {x:x for x in numeros}
        g = tablero.juego(dsimbolos)
        tablero.actualiza_score(score,g)
       
 
if __name__ == '__main__':
    main()
   