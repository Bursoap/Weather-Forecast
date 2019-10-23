from apps.forecast.models import Forecast
from managers import MarshmallowManager, DatabaseManager

db = DatabaseManager.db
ma = MarshmallowManager.ma


class ForecastSchema(ma.ModelSchema):

    class Meta:
        model = Forecast
        sqla_session = db.session


forecast_schema = ForecastSchema()
