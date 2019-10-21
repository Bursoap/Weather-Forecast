from settings import Config


class LocalConfig(Config):
    DEVELOPMENT = True
    TESTING = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'CHANGE-IN-PRODUCTION'
    HOST = 'localhost'
    PORT = 5000
