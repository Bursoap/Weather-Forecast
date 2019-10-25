from flask import Blueprint
from flask_restful import Api

city_blueprint = Blueprint(
    'city',
    __name__,
    url_prefix='/api/city/'
)

api = Api(city_blueprint)
from .routes import register_routes
register_routes(api)
