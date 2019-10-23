from flask import render_template
from flask.views import MethodView

from apps.city.models import City
from apps.forecast.models import Forecast
from apps.city.schemas.city import city_schema


class ForecastTemplateView(MethodView):

    template_name = 'forecast/forecast.html'

    def get(self):
        city = City.query.first()
        data = city_schema.dump(city)
        return render_template(self.template_name)

