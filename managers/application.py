class ApplicationManager:

    @classmethod
    def register_applications(cls, app):
        from apps.city import city_api_blueprint
        from apps.forecast import forecast_blueprint, forecast_api_blueprint

        app.register_blueprint(city_api_blueprint)
        app.register_blueprint(forecast_blueprint)
        app.register_blueprint(forecast_api_blueprint)
