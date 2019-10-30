from flask import request
from flask_restful import Resource
from apps.forecast.schemas.forecast import forecast_schema
from apps.forecast.services.create_forecast import CreateForecastService
from apps.forecast.services.get_forecast import GetForecastService


class ForecastAPIView(Resource):

    def get(self):
        city_id = request.args.get('city_id')
        forecasts = GetForecastService().get_forecast(city_id)

        if not forecasts:
            forecasts = CreateForecastService().create_forecast(city_id)

        return forecast_schema.dump(forecasts, partial=True)
