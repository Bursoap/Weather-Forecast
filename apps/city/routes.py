from apps.city.views import CitiesAutocompleteView


def register_routes(api):
    api.add_resource(CitiesAutocompleteView, 'autocomplete',
                     endpoint='cities_autocomplete')
