'''
FUNCIONES AUXILIARES PARA EL PROGRAMA "LÍNEA"
'''

def calcular_y(x, m, b):
    '''
    Calcula "y" de acuerdo a la pendiente "m" y
    el punto de intersección en "A" y "B"
    retornando el valor de "y"
    '''
    return m*x+b

if __name__ == "__main__":
    x = 0
    m = 3
    b = 2
    y = calcular_y(x, m, b)

    print(y)

    if y == 2:
        print("Prueba exitosa :3")
    else:
        print("Prueba fallida u.u")