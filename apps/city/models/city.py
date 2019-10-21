from managers import DatabaseManager

db = DatabaseManager.db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(2), nullable=False)
    lon = db.Column(db.Numeric(9, 6), nullable=False)
    lat = db.Column(db.Numeric(9, 6), nullable=False)

    def __repr__(self):
        return f'<City id={self.id} name={self.name}>'
