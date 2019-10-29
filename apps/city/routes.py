from apps.city.api_views import CitiesAutocompleteView


def register_api_routes(api):
    api.add_resource(CitiesAutocompleteView, 'autocomplete',
                     endpoint='cities_autocomplete')
