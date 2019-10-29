from flask import render_template
from flask.views import MethodView


class ForecastTemplateView(MethodView):

    template_name = 'forecast/forecast.html'

    def get(self):
        return render_template(self.template_name)
