from flask import request
from flask_restful import Resource
from apps.forecast.models import Forecast
from apps.forecast.schemas.forecast import forecast_schema


class ForecastAPIView(Resource):

    def get(self):
        city_id = request.args.get('city_id')
        forecasts = Forecast.query.all()
        return forecast_schema.dump(forecasts, many=True)
