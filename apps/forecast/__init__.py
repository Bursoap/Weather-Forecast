from flask import Blueprint

forecast_blueprint = Blueprint(
    'forecasts',
    __name__,
    url_prefix='/forecasts/'
)

from .routes import *
