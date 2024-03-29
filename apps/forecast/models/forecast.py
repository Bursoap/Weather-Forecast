from managers import DatabaseManager

db = DatabaseManager.db


class Forecast(db.Model):
    __table_args__ = (
        db.UniqueConstraint('city_id', 'forecast_date', name='unique_forecast'),
    )

    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    city = db.relationship('City', backref='forecasts')

    forecast_date = db.Column(db.Date, nullable=False)
    main = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    temp = db.Column(db.Float(4), nullable=False)
    temp_min = db.Column(db.Float(4), nullable=False)
    temp_max = db.Column(db.Float(4), nullable=False)
    pressure = db.Column(db.Float(6), nullable=False)
    sea_level = db.Column(db.Float(6), nullable=False)
    grnd_level = db.Column(db.Float(6), nullable=False)
    humidity = db.Column(db.Integer, nullable=False)
    clouds = db.Column(db.Integer)
    wind_speed = db.Column(db.Float(5))
    wind_degrees = db.Column(db.Integer)
    rain_mm = db.Column(db.Integer)
    snow_mm = db.Column(db.Integer)

    def __repr__(self):
        return f'<Forecast id={self.id} city_id={self.city_id}>'
