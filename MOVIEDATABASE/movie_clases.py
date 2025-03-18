'''
CLASES DEL SISTEMA DE PELÍCULAS, ACTORES Y ACTRICES
'''

import csv
import hashlib
from datetime import datetime


class Actor:
    ''' CLASE ACTOR '''

    def __init__(self, id_estrella, nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen, username):
        ''' CONSTRUCTOR DE LA CLASE ACTOR '''
        self.id_estrella            = id_estrella
        self.nombre                 = nombre
        self.fecha_nacimiento       = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
        self.ciudad_nacimiento      = ciudad_nacimiento
        self.url_imagen             = url_imagen
        self.username               = username

    def to_dict(self):
        ''' DEVUELVE UN DICCIONARIO CON LOS DATOS DEL ACTOR '''
        return {
            'id_estrella'           : self.id_estrella,
            'nombre'                : self.nombre,
            'fecha_nacimiento'      : self.fecha_nacimiento.strftime('%Y-%m-%d'),
            'ciudad_nacimiento'     : self.ciudad_nacimiento,
            'url_imagen'            : self.url_imagen,
            'username'              : self.username
        }
    

class Pelicula:
    ''' CLASE PELÍCULA '''

    def __init__(self, id_pelicula, titulo_pelicula, fecha_lanzamiento, url_poster):
        ''' CONSTRUCTOR DE LA CLASE PELÍCULA '''
        self.id_pelicula            = id_pelicula
        self.titulo_pelicula        = titulo_pelicula
        self.fecha_lanzamiento      = datetime.strptime(fecha_lanzamiento, '%Y-%m-%d')
        self.url_poster             = url_poster

    def to_dict(self):
        ''' DEVUELVE UN DICCIONARIO CON LOS DATOS DE LA PELÍCULA '''
        return {
            'id_pelicula'           : self.id_pelicula,
            'titulo_pelicula'       : self.titulo_pelicula,
            'fecha_lanzamiento'     : self.fecha_lanzamiento.strftime('%Y-%m-%d'),
            'url_poster'            : self.url_poster
        }
    

class Relacion:
    ''' CLASE RELACIÓN: RELACIÓN ENTRE ACTORES Y PELÍCULAS '''

    def __init__(self, id_relacion, id_pelicula, id_estrella):
        ''' CONSTRUCTOR DE LA CLASE RELACIÓN '''
        self.id_relacion            = id_relacion
        self.id_pelicula            = id_pelicula
        self.id_estrella            = id_estrella

    def to_dict(self):
        ''' DEVUELVE UN DICCIONARIO CON LOS DATOS DE LA RELACIÓN '''
        return {
            'id_relacion'           : self.id_relacion,
            'id_pelicula'           : self.id_pelicula,
            'id_estrella'           : self.id_estrella
        }
    

class User:
    ''' CLASE USER: USUARIO DEL SISTEMA '''

    def __init__(self, username, nombre_completo, email, password):
        ''' CONSTRUCTOR DE LA CLASE USUARIO '''
        self.username               = username
        self.nombre_completo        = nombre_completo
        self.email                  = email
        self.password               = self.hash_password(password.encode()).hexdigest()

    def hash_password(self, password):
        ''' MÉTODO PARA ENCRIPTAR UNA CONTRASEÑA '''
        return sha256(password.encode()).hexdigest()
    
    def to_dict(self):
        ''' DEVUELVE UN DICCIONARIO CON LOS DATOS DEL USUARIO '''
        return {
            'username'              : self.username,
            'nombre_completo'       : self.nombre_completo,
            'email'                 : self.email,
            'password'              : self.password
        }
    

class SistemaCine:
    ''' CLASE SISTEMA CINE: SISTEMA DE PELÍCULAS '''
    
    def __init__(self):
        ''' CONSTRUCTOR DE LA CLASE SISTEMA CINE '''
        self.actores                = []
        self.peliculas              = []
        self.relaciones             = []
        self.usuarios               = []
        self.usuario_actual         = None

    def cargar_csv(self, archivo, clase):   
        ''' MÉTODO PARA CARGAR DATOS DESDE UN ARCHIVO CSV '''
        with open(archivo, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if clase == Actor:
                    self.actores.append(Actor(**row))
                elif clase == Pelicula:
                    self.peliculas.append(Pelicula(**row))
                elif clase == Relacion:
                    self.relaciones.append(Relacion(**row))
                elif clase == User:
                    self.usuarios.append(User(**row))