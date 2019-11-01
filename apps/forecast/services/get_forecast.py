import datetime


class GetForecastService:

    def __init__(self):
        self.forecast_dates = self.get_forecast_dates()

    def get_forecast(self, city_id):
        # query = self.model.query.filter(
        #     self.model.city_id == city_id,
        #     self.model.forecast_date.in_(self.forecast_dates)
        # )
        #
        # if query.count() >= 5:
        #     return query.all()

        return []

    @staticmethod
    def get_forecast_dates():
        forecast_dates = []
        today = datetime.datetime.now().date()

        for days_diff in range(1, 6):
            forecast_date = today + datetime.timedelta(days=days_diff)
            forecast_dates.append(forecast_date)

        return forecast_dates
