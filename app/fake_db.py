from app.models import Route, Flight, Airport
from app import db

def add_routes():
    # Only run if route DB is empty
    if not Route.query.first():
        # Example of adding five fake routes
        routes = [
            Route(origin='SFO', destination='LAX'),
            Route(origin='LAX', destination='SFO'),
            Route(origin='SFO', destination='OAK'),
            Route(origin='OAK', destination='SFO'),
            Route(origin='SFO', destination='SJC'),
            Route(origin='SJC', destination='SFO')
        ]
        
        # Add each route manually into DB
        for route in routes:
            db.session.add(route)
        db.session.commit()

def add_flights():
    # Only run if the flight DB is empty
    if not Flight.query.first():
        # Example of adding five fake flights
        flights = [
            Flight(flight_number=101, route_id=1, weather_description='Clear skies', airline_name='DELTA', aircraft_model="B737MAX", price=230),
            Flight(flight_number=102, route_id=1, weather_description='Light rain', airline_name='SPIRIT', aircraft_model="A320NEO", price=254),
            Flight(flight_number=103, route_id=2, weather_description='Heavy rain', airline_name='SOUTHWEST', aircraft_model="B777X", price=390),
            Flight(flight_number=104, route_id=2, weather_description='Sunny', airline_name='DELTA', aircraft_model="A321XLR", price=1020),
            Flight(flight_number=105, route_id=3, weather_description='Cloudy', airline_name='UNITED', aircraft_model="G800", price=50)
        ]
        
        # Add each airport manually into DB
        for flight in flights:
            db.session.add(flight)
        db.session.commit()

def add_airports():
    # Only run if the airport DB is empty
    if not Airport.query.first():  # Check if the database is empty
        airports = [
            Airport(airport_code='SFO', terminal_info='Terminals 1, 2, and International Terminal', timezone='America/Los_Angeles', runway_info='Runways 1L/19R, 1R/19L, 28L/10R, 28R/10L', url_link='https://www.flysfo.com/'),
            Airport(airport_code='LAX', terminal_info='Terminal 1 to Terminal 8', timezone='America/Los_Angeles', runway_info='Runway 24L/06R, Runway 24R/06L', url_link='https://www.flylax.com/'),
            Airport(airport_code='SJC', terminal_info='Terminal A and Terminal B', timezone='America/Los_Angeles', runway_info='Runway 12L/30R, Runway 12R/30L', url_link='https://www.flysanjose.com/'),
            Airport(airport_code='OAK', terminal_info='Terminal 1 and Terminal 2', timezone='America/Los_Angeles', runway_info='Runway 12/30, Runway 10/28', url_link='https://www.oaklandairport.com/'
            )
        ]
        # Add each flight manually into DB
        for airport in airports:
            db.session.add(airport)
        db.session.commit()