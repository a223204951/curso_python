'''
HOLA MUNDO DE FLASK !! :3
'''
from flask import Flask
app = Flask(__name__)

@app.route('/') # HOME PAGE O RAÍZ O ÍNDICE
def index():
    return '''<html>
                <head>
                    <title> Hello World !! :3 </title>
                </head>
                        <body><h1> Hola Mundo !! :3 </h1>
                        <p> Ir a la página de <a href="/about">Acerca de</a></p>
                        </body>
            </html>'''

@app.route('/about') # ACERCA DE...
def index():
    return '''<html>
                <head>
                    <title> Acerca de...</title>
                </head>
                        <body><h1> Acerca de Lani !! :3</h1>
                        <p> Ir a la página de <a href="/about">Inicio</a></p>
                        </body>
            </html>'''

if __name__ == '__main__':
    app.run(debug=True) #Activar el modo de depuración