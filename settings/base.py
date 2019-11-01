import os


class Config:
    DEBUG = False
    SECRET_KEY = 'this-really-needs-to-be-changed'
    MONGO_URI = os.environ['MONGO_URI']
