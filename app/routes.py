from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from flask import request

from app import obj
from app.forms import routeForm, flightForm

from app.models import Ticket, Route, Flight, Airport
from app import db

# Route to show airport information
@obj.route("/")
def home_page():
    # Retrieve all airports from the database
    all_airports = Airport.query.all()

    return render_template("home.html", airports=all_airports)

# Route to show all the flights listed by airport, and flight information (weather, airline, etc.)
@obj.route("/flights")
def flights_page():
    routes = Route.query.all()  # Fetch all routes
    flight_info = {}
    # Get the corresponding route ID to the flight
    for route in routes:
        # Creates a new origin/airport without duplicates
        if route.origin not in flight_info:
            flight_info[route.origin] = []

        # For all flights corresponding to the route ID, add it to matching route origin
        for flight in Flight.query.filter_by(route_id=route.route_id).all():
            flight_info[route.origin].append(flight)
        
    print(flight_info)

    return render_template("book_flights.html", flight_info=flight_info)

# Route to book a flight and make a ticket
@obj.route("/book-flight/<int:flight_number>", methods=["POST"])    
def book_flight(flight_number):
    if flight_number:
            # Get the flight the user clicked
            flight = Flight.query.get(flight_number)
            print(f"Booking flight #{flight.flight_number} for ${flight.price}")

            # Make a ticket based on their flight_number they booked
            new_ticket = Ticket(flight_number=flight_number)
            db.session.add(new_ticket)
            db.session.commit()
            flash(f"Successful: Booked Flight #{flight_number}")
            return redirect(url_for("bookings_page"))

    return redirect(url_for("book_flights"))

# Ticket page
@obj.route("/bookings")
def bookings_page():
    # Get all the tickets in order to render
    tickets = Ticket.query.all()
    return render_template("bookings.html", tickets=tickets)

# Route to modify ticket
@obj.route("/edit-booking/<int:ticket_number>", methods=["POST"])
def edit_booking(ticket_number):
    # Get the ticket the user is trying to modify
    ticket = Ticket.query.get(ticket_number)

    # Get the new seat the user chose from the button
    changed_seat = request.form.get("new_seat_class")
    # Make changes to the ticket database
    ticket.seat_class = changed_seat
    db.session.commit()
    flash(f"Successful: Edited Ticket #{ticket_number} to {changed_seat}")
    return redirect(url_for("bookings_page"))

# Route to delete ticket
@obj.route("/delete-booking/<int:ticket_number>", methods=["POST"])
def delete_booking(ticket_number):
    # Get the ticket the user is trying to delete and delete from database
    ticket = Ticket.query.get(ticket_number)
    db.session.delete(ticket)
    db.session.commit()
    flash(f"Successful: Deleted Ticket #{ticket.ticket_number}, Flight #{ticket.flight_number}")
    return redirect(url_for("bookings_page"))

# Route to add to airline routes and flights
@obj.route("/add", methods=["GET", "POST"])
def add_page():
    # Create two add forms 
    route_form = routeForm()
    flight_form = flightForm()

    # Check to see if user clicked the submit route button
    if route_form.validate_on_submit():
        new_origin = route_form.origin.data.upper()
        new_destination = route_form.destination.data.upper()

        # Checks if origin and destination are IATA codes or length of 3
        if (len(new_origin) != 3 or len(new_destination) != 3):
            flash("Unsuccessful: Origin and Destination should be IATA Codes (length of 3)")
            return redirect("/add")
    
        # Check for duplicate records in database
        routes = Route.query.all()
        for route in routes:
            if route.origin == new_origin and route.destination == new_destination:
                flash("Unsuccessful: Duplicate route detected")
                return redirect("/add")
            
        # Create a new route in database
        new_route = Route(origin=new_origin, destination=new_destination)
        db.session.add(new_route)
        db.session.commit()
        flash(f"Successful: Added a new route in the database from {new_origin} to {new_destination}")

    # Check to see if user clicked the submit flight button
    if flight_form.validate_on_submit():
        new_origin = flight_form.flight_origin.data.upper() 
        new_destination = flight_form.flight_destination.data.upper()
        new_flight_number = flight_form.flight_number.data
        new_weather_description = flight_form.weather_description.data
        new_aircraft_model = flight_form.aircraft_model.data.upper() # Used .upper() to fix formatting in DB
        new_airline_name = flight_form.airline_name.data.upper() 
        new_price = flight_form.price.data

        # Checks if origin and destination are IATA codes or length of 3
        if (len(new_origin) != 3 or len(new_destination) != 3):
            flash("Unsuccessful: Origin and Destination should be IATA Codes (length of 3)")
            return redirect("/add")
        
        # Check if there is an existing flight number already
        flights = Flight.query.all()
        for flight in flights:
            if flight.flight_number == new_flight_number:
                flash(f"Unsuccessful: Flight #{flight.flight_number} already in system")
                return redirect("/add")

        # Check if origin and destination are in the Route database
        flight_routes = Route.query.all()
        for route in flight_routes:
            if route.origin == new_origin and route.destination == new_destination:
                # Find the route ID based on the origin and destination the user inputted
                route = Route.query.filter_by(origin=new_origin, destination=new_destination).first()

                # Create new Flight in database based on all data collected
                new_flight = Flight(flight_number=new_flight_number, route_id=route.route_id, weather_description=new_weather_description, aircraft_model=new_aircraft_model, airline_name=new_airline_name, price=new_price)
                db.session.add(new_flight)
                db.session.commit()
                flash("Successful: New route added")
                return redirect("/add")
        
        flash("Unsuccessful: Origin and destination not in the system")
        return redirect("/add")
            
    return render_template("add_page.html", route_form=route_form, flight_form=flight_form)





