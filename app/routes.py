from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from flask import request
from app import obj

from app.models import Ticket, Route, Flight, Airport
from app import db


@obj.route("/")
def home_page():
    # Retrieve all airports from the database
    all_airports = Airport.query.all()

    return render_template("home.html", airports=all_airports)

@obj.route("/flights")
def flights_page():
    # Get the corresponding route ID to the flight
    routes = Route.query.all()  # Fetch all routes
    flight_info = {}
    for route in routes:
        # Doesn't create duplicate flight information
        if route.origin not in flight_info:
            flight_info[route.origin] = []

        # For all flights corresponding to the route ID, add it to matching route origin
        for flight in Flight.query.filter_by(route_id=route.route_id).all():
            flight_info[route.origin].append(flight)
        
    print(flight_info)

    return render_template("flights.html", flight_info=flight_info)

@obj.route("/book-flight/<int:flight_number>", methods=['POST'])    
def book_flight(flight_number):
    if flight_number:
            # Get the flight the user clicked
            flight = Flight.query.get(flight_number)
            print(f"Booking flight #{flight.flight_number} for ${flight.price}")

            # Make a ticket based on their flight_number they booked
            new_ticket = Ticket(flight_number=flight_number, status="Confirmed")
            db.session.add(new_ticket)
            db.session.commit()
            flash('Booking successfully added.', 'success')
            return redirect(url_for("bookings_page"))

    return redirect(url_for('flights_page'))

@obj.route("/bookings", methods=['GET'])
def bookings_page():
    # Get all the tickets in order to render
    tickets = Ticket.query.all()
    return render_template("bookings.html", tickets=tickets)

@obj.route("/edit-booking/<int:ticket_number>", methods=['POST'])
def edit_booking(ticket_number):
    # Get the ticket the user is trying to modify
    ticket = Ticket.query.get(ticket_number)

    # Get the new seat from the form data and change to db
    changed_seat = request.form.get('new_seat_class')
    ticket.seat_class = changed_seat
    db.session.commit()

    flash('Booking successfully updated.', 'success')
    return redirect(url_for('bookings_page'))


@obj.route("/delete-booking/<int:ticket_number>", methods=['POST'])
def delete_booking(ticket_number):
    # Get the ticket the user is trying to delete and delete from database
    ticket = Ticket.query.get(ticket_number)
    db.session.delete(ticket)
    db.session.commit()
    flash('Booking successfully deleted.', 'success')
    return redirect(url_for('bookings_page'))
