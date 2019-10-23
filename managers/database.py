from flask_sqlalchemy import SQLAlchemy


class DatabaseManager:
    db = None

    @classmethod
    def setup_db(cls, app):
        cls.db = SQLAlchemy(app)
        return cls.db
