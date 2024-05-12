from app.models import Ticket, Route, Flight
from app import db

def add_tickets():
    # Only run if ticket DB is empty
    if not Ticket.query.first():
        # Example of adding five more fake tickets
        tickets = [
            Ticket(ticket_number=1002, flight_number=1, price=250, seat_class='Economy'),
            Ticket(ticket_number=1003, flight_number=1, price=300, seat_class='Business'),
            Ticket(ticket_number=1004, flight_number=2, price=220, seat_class='Economy'),
            Ticket(ticket_number=1005, flight_number=2, price=350, seat_class='Business'),
            Ticket(ticket_number=1006, flight_number=3, price=400, seat_class='First Class')
        ]

        # Add each airport manually into DB
        for ticket in tickets:
            db.session.add(ticket)
        db.session.commit()

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
            Flight(flight_number=101, route_id=1, weather_description='Clear skies', airline_name='Airline A', aircraft_model='Boeing 737'),
            Flight(flight_number=102, route_id=1, weather_description='Light rain', airline_name='Airline B', aircraft_model='Airbus A320'),
            Flight(flight_number=103, route_id=2, weather_description='Heavy rain', airline_name='Airline C', aircraft_model='Boeing 747'),
            Flight(flight_number=104, route_id=2, weather_description='Sunny', airline_name='Airline D', aircraft_model='Boeing 777'),
            Flight(flight_number=105, route_id=3, weather_description='Cloudy', airline_name='Airline E', aircraft_model='Airbus A380')
        ]
        
        # Add each flight manually into DB
        for flight in flights:
            db.session.add(flight)
        db.session.commit()
