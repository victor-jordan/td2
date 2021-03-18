import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Taller de Desarrollo 2</h1><p>Prototipo de API para la catedra de desarrollo 2.</p>"


app.run()
