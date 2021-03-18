from flask import Flask, jsonify, make_response, render_template
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

app = Flask(__name__)
bd_uri = 'mysql+pymysql://freedbtech_victorj:unasur2016@freedb.tech:3306/freedbtech_unasurpruebas'
app.config['SQLALCHEMY_DATABASE_URI'] = bd_uri
db = SQLAlchemy(app)


# Mapeamos la tabla de la base de datos con sqlalchemy
class Producto(db.Model):
    __tablename__ = 'producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    precio = db.Column(db.Integer)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return '' % self.id


# Le damos un esquema para poder serializar en formato JSON
class ProductoSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Producto
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    nombre = fields.String(required=True)
    precio = fields.Number(required=True)


@app.route('/productos', methods=['GET'])
def api():
    get_productos = Producto.query.all()  # select * from producto
    producto_schema = ProductoSchema(many=True)
    productos = producto_schema.dump(get_productos)
    return make_response(jsonify({"productos": productos}))


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
