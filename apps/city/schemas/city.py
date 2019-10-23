from apps.city.models import City
from managers import MarshmallowManager, DatabaseManager

db = DatabaseManager.db
ma = MarshmallowManager.ma


class CitySchema(ma.ModelSchema):

    class Meta:
        model = City
        exclude = ('id', )
        unknown = 'EXCLUDE'
        sqla_session = db.session


city_schema = CitySchema()
