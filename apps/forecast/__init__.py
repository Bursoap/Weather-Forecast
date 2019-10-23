from flask import Blueprint

forecast_blueprint = Blueprint(
    'forecasts',
    __name__,
    url_prefix='/'
)

from .routes import register_routes
register_routes(forecast_blueprint)
