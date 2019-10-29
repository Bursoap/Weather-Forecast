from flask import Blueprint
from flask_restful import Api

forecast_blueprint = Blueprint(
    'forecast',
    __name__,
    url_prefix='/'
)

forecast_api_blueprint = Blueprint(
    'forecast_api',
    __name__,
    url_prefix='/api/forecast/'
)

api = Api(forecast_api_blueprint)

from .routes import register_routes, register_api_routes
register_routes(forecast_blueprint)
register_api_routes(api)
