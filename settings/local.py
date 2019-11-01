from settings import Config


class LocalConfig(Config):
    DEVELOPMENT = True
    TESTING = True
    DEBUG = True
    SECRET_KEY = 'CHANGE-IN-PRODUCTION'
    HOST = 'localhost'
    PORT = 5000
