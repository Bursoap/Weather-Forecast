from flask_marshmallow import Marshmallow


class MarshmallowManager:
    ma = None

    @classmethod
    def setup_ma(cls, app):
        cls.ma = Marshmallow(app)
        return cls.ma
