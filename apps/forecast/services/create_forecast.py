import os
import datetime

import requests

from apps.forecast.schemas.forecast import forecast_schema


def flatten(d):
    out = {}

    for key, value in d.items():
        if isinstance(value, dict):
            out.update(flatten(value))
            continue
        out[key] = value

    return out


class CreateForecastService:

    API_KEY = os.environ.get('API_KEY')
    API_URL = os.environ.get('API_URL')

    def create_forecast(self, city_id):
        response = self.make_request(city_id)
        forecast_dicts = self.extract_forecast_dicts(response)
        forecasts = forecast_schema.load(forecast_dicts, many=True)
        return

    def make_request(self, city_id):
        payload = {
            'APPID': self.API_KEY,
            'id': city_id,
            'units': 'metric',
        }

        response = requests.get(self.API_URL, params=payload)
        if response.status_code != requests.codes.ok:
            response.raise_for_status()

        return response

    @staticmethod
    def extract_forecast_dicts(response):
        processed_dates = []
        forecast_dicts = []

        for forecast_dict in response.json().get('list'):
            forecast_date = datetime.datetime\
                .strptime(forecast_dict.get('dt_txt'), '%Y-%m-%d %H:%M:%S')\
                .date()

            if forecast_date in processed_dates:
                continue

            flatten_forecast_dict = flatten(forecast_dict)
            flatten_forecast_dict['forecast_date'] = forecast_date
            forecast_dicts.append(flatten_forecast_dict)
            processed_dates.append(forecast_date)

        return forecast_dicts
