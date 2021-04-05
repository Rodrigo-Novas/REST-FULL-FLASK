"""
Un esquema sirve para serializar objetos y pasarlos a json o viceversa en este caso para serializar se va a utilizar marshmallow
Las clases deben ser esquemas que coincidan con la cantidad y nombre de los campos de las tablas que creamos dentro de models

"""

from marshmallow import fields

from app.ext import ma


class FilmSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    length = fields.Integer()
    year = fields.Integer()
    director = fields.String()
    actors = fields.Nested('ActorSchema', many=True)


class ActorSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()