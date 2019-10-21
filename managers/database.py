from flask_sqlalchemy import SQLAlchemy


class DatabaseManager:
    db = None

    @classmethod
    def setup_db(cls, app):
        cls.db = SQLAlchemy(app)
        cls.register_models()
        return cls.db

    @classmethod
    def register_models(cls):
        # ToDo Needs to make models visible for migrations
        from apps.city.models import City
        from apps.forecast.models import Forecast
