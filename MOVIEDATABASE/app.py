# Programa principal de movieDatabase
from flask import Flask, render_template, request, redirect, url_for
import random
import os
import movie_clases as mc

app = Flask(__name__)
sistema = mc.SistemaCine()
ruta = 'datos/'
actores_csv = ruta + 'actores.csv'
peliculas_csv = ruta + 'peliculas.csv'
relaciones_csv = ruta + 'relacion.csv'
users_csv = ruta + 'users.csv'
sistema.cargar_csv(actores_csv,mc.Actor)
sistema.cargar_csv(peliculas_csv,mc.Pelicula)
sistema.cargar_csv(relaciones_csv,mc.Relacion)
sistema.cargar_csv(users_csv,mc.User)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/actores')
def actores():
    
    return render_template('templates/actores.html', actores = sistema.actores)

@app.route('/peliculas')
def peliculas():
    lista_peliculas = sistema.peliculas.values()
    return render_template('peliculas.html', peliculas = lista_peliculas)


if __name__ == '_main_':
    app.run(debug=True)
    