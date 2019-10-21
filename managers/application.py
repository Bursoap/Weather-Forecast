class ApplicationManager:

    @classmethod
    def register_applications(cls, app):
        from apps.forecast import forecast_blueprint

        app.register_blueprint(forecast_blueprint)
