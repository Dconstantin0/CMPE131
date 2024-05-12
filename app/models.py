from app import db

# Model for our ticket DB
class Ticket(db.Model):
    ticket_number = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.Integer, db.ForeignKey('flight.flight_number'))
    price = db.Column(db.Integer)
    seat_class = db.Column(db.String(10))

    flight = db.relationship('Flight', backref='tickets')

# Model for our Route DB
class Route(db.Model):
    route_id = db.Column(db.Integer, primary_key=True)
    # IATA Codes to determine
    origin = db.Column(db.String(3)) 
    destination = db.Column(db.String(3))

# Model for our Flight DB
class Flight(db.Model):
    flight_number = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.route_id'))
    weather_description = db.Column(db.String(200))  # Embedded weather
    airline_name = db.Column(db.String(100))  # Simplified airline info
    aircraft_model = db.Column(db.String(100))  # Simplified aircraft info

    route = db.relationship('Route', backref='flights')

