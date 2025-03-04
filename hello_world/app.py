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
                        <body><h1> Hola Mundo !! :3 </h1>
                        <p> Ir a la página de <a href="/about">Acerca de</a></p>
                        </body>
                </head>
            </html>'''

@app.route('/') # HOME PAGE O RAÍZ O ÍNDICE
def index():
    return '''<html>
                <head>
                    <title> Hello World !! :3 </title>
                        <body><h1> Hola Mundo !! :3 </h1>
                        <p> Ir a la página de <a href="/about">Acerca de</a></p>
                        </body>
                </head>
            </html>'''