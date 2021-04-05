"""
Para implementar los recursos en Flask haremos uso de la extensión Flask-Restful. En Flask-Restful
un recurso no es más que una clase asociada a un endpoint (la URL mediante la que se expone el recurso)
que define cómo se puede acceder y/o manipular dicho recurso. Para ello, 
solo hay que implementar los métodos correspondientes a cada uno de los verbos HTTP que se necesiten.
las clases que se vana  ver a continuacion forman parte de los protocolos
"""
from flask import request, Blueprint
from flask_restful import Api, Resource
from .schemas import FilmSchema
from ..models import Film, Actor

films_v1_0_bp = Blueprint('films_v1_0_bp', __name__)
film_schema = FilmSchema()
api = Api(films_v1_0_bp)


class FilmResource(Resource):
    """
    Solamente un get que obtiene el film por id
    """
    def get(self, film_id):
        film = Film.get_by_id(film_id)
        if film is None:
            raise ObjectNotFound('La película no existe')
        resp = film_schema.dump(film)
        return resp

class FilmListResource(Resource):
    """
    Permite hacer peticiones get y post, deben heradar siempre de Resources
    """
    def get(self):
        """
        Se establece un get
        """
        films = Film.get_all()
        if films is None:
            raise ObjectNotFound('La película no existe')
        result = film_schema.dump(films, many=True)
        return result

    def post(self):
        """
        Se establece un post
        En primer lugar obtiene el cuerpo de la respuesta en formato JSON. Para ello, se llama al método get_json() del objeto request.
        A continuación se llama al método load() del esquema film_schema. Este método valida que el JSON data cumpla con el esquema. 
        A su vez, se crea el diccionario film_dict a partir del JSON original.
        Se crea una instancia de Film a partir de los datos del diccionario y se guarda.
        Se serializa el objeto film y se devuelve en la respuesta. Fíjate que en esta ocasión también se indica el código de respuesta. 
        En este caso 201, que significa que se creó un objeto.
        """
        data = request.get_json()
        film_dict = film_schema.load(data)
        film = Film(title=film_dict['title'],
                    length=film_dict['length'],
                    year=film_dict['year'],
                    director=film_dict['director']
        )
        for actor in film_dict['actors']:
            film.actors.append(Actor(actor['name']))
        film.save()
        resp = film_schema.dump(film)
        return resp, 201

api.add_resource(FilmListResource, '/api/v1.0/films/', endpoint='film_list_resource')
api.add_resource(FilmResource, '/api/v1.0/films/<int:film_id>', endpoint='film_resource')