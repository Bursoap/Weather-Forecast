from apps.forecast.views import ForecastTemplateView


def register_routes(bp):
    bp.add_url_rule('', view_func=ForecastTemplateView.as_view('forecasts'),
                    endpoint='forecasts')
