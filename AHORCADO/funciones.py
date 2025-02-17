'''
funciones auxilaries para el juego del ahorcado
'''
 
import abc
from random import choice
import string
import unicodedata


def carga_archivo_texto(archivo:str)->list:
    '''Carga un arcihivo de texto y devuelve una lista con las oraciones del archivo'''
 
    with open(archivo, 'r', encoding='utf-8') as f:
        oraciones = f.readlines()
    return oraciones
 
 
def carga_plantillas(nombre_plantilla:str) -> dict:
    '''
    Carga las plantillas del juego a partir de un archivode texto
    '''
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'./AHORCADO/PLANTILLAS/{nombre_plantilla}-{i}.txt')
    return plantillas
 
def despliega_plantilla(diccionario:dict, nivel:int):
    '''
    Despliega una plantilla del juego
    '''
 
    if nivel in diccionario:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)
 
def obten_palabras(lista:str)->list:
    '''
    Obtiene las palabras de un texto
    '''
    texto = ' '.join(lista[120:])
    palabras = texto.split()
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    #removemos signos de puntuacion y caracteres especiales
    set_palabras = {palabra.strip(string.punctuation) for palabra in set_palabras}
    #removemos números, paréntesis, corchetes, etc
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}
    #removemos acentos
    set_palabras = {unicodedata.normalize('NFKD', palabra).encode('ASCII', 'ignore').decode('ascii') for palabra in set_palabras}
    return list(set_palabras)

def adivina_letra(abc:dict, palabra:str, letras_adivinadas:set, turnos:int)->int:
    '''
    Adivina una letra de la palabra
    '''
    palabra_oculta = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += '_'
    print(f'Tienes {turnos} oportunidades de fallar')
    abcd = ' '.join(abc.values())
    print(f'El abecedario es: {abcd}')
    print(f'La palabra es: {palabra_oculta}')
    letra = input('Dame una letra: ')
    letra = letra.lower()
    if letra in abc:
        if abc[letra] == "*":
            print('Esa letra ya la habias adivinado')
        else:
            abc[letra] = '*'
            if letra in palabra:
                letras_adivinadas.add(letra)
            else:
                turnos -= 1
                print(f'La letra {letra} no está en la palabra')
    return turnos
 
if __name__ == '__main__':
    plantillas = carga_plantillas('plantilla')
    despliega_plantilla(plantillas, 5)
    lista_oraciones = carga_archivo_texto('./AHORCADO/DATOS/pg15532.txt')
    lista_palabras = obten_palabras(lista_oraciones)
    p = choice(lista_palabras)
    print(p)
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    t = 5 #oportunidades
    t = adivina_letra(abcdario, p, adivinadas, t)
    print(t)
    t = adivina_letra(abcdario, p, adivinadas, t)
    print(t)
    adivina_letra(abcdario, p, adivinadas, t)
    adivina_letra(abcdario, p, adivinadas, t)
    #print(lista_palabras[:50])