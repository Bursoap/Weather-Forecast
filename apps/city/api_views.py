from flask import request
from flask_restful import Resource

from apps.city.models import City
from apps.city.schemas.city import city_schema


class CitiesAutocompleteView(Resource):

    def get(self):
        name = request.args.get('name', 'default_name')
        cities = City.query.filter(City.name.ilike(f'{name}%')).limit(10).all()
        return city_schema.dump(cities, many=True)
