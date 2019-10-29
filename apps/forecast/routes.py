from apps.forecast.views import ForecastTemplateView
from apps.forecast.api_views import ForecastAPIView


def register_routes(bp):
    bp.add_url_rule('', view_func=ForecastTemplateView.as_view('forecasts'),
                    endpoint='forecasts')


def register_api_routes(api):
    api.add_resource(ForecastAPIView, '', endpoint='get_forecast')
