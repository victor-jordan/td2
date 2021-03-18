import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Cramos datos de prueba en forma de lista de diccionarios
usuarios = [
    {'id': 1,
     'username': 'admin',
     'email': 'admin@prueba.com'},
    {'id': 2,
     'username': 'usuario1',
     'email': 'usuario1@prueba.com'},
    {'id': 3,
     'username': 'usuario2',
     'email': 'usuario2@prueba.com'}
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Taller de Desarrollo 2</h1><p>Prototipo de API para la catedra de desarrollo 2.</p>"


# Una ruta que retorne todas las entradas de nuestro catálogo en usuarios
@app.route('/api/v1/resources/usuarios/all', methods=['GET'])
def api_all():
    return jsonify(usuarios)


app.run()
