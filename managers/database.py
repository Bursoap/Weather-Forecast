from flask_pymongo import PyMongo


class DatabaseManager:
    db = None

    @classmethod
    def setup_db(cls, app):
        cls.db = PyMongo(app)
        return cls.db
