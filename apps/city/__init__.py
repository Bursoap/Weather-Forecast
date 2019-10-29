from flask import Blueprint
from flask_restful import Api

city_api_blueprint = Blueprint(
    'city_api',
    __name__,
    url_prefix='/api/city/'
)

api = Api(city_api_blueprint)
from .routes import register_api_routes
register_api_routes(api)
