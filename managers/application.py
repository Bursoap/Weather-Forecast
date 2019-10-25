class ApplicationManager:

    @classmethod
    def register_applications(cls, app):
        from apps.city import city_blueprint
        from apps.forecast import forecast_blueprint

        app.register_blueprint(city_blueprint)
        app.register_blueprint(forecast_blueprint)
