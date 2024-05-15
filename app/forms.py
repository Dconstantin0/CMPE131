from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

# Route form to add a new route to the system
class routeForm(FlaskForm):
    origin = StringField('Origin', validators=[DataRequired()])
    destination = StringField('Destination', validators=[DataRequired()])
    submit = SubmitField('Submit Route')


class airportForm(FlaskForm):
    airport_code = StringField('Airport IATA', validators=[DataRequired()])
    airport_timezone = StringField('Airport Timezone', validators=[DataRequired()])
    airport_terminal = StringField('Airport Terminal', validators=[DataRequired()])
    airport_runways = StringField('Airport Runways', validators=[DataRequired()])
    airport_url = StringField('Airport URL', validators=[DataRequired()])
    submit = SubmitField('Submit Airport')


# Flight form to add a new flight to the system
class flightForm(FlaskForm):
    # Use these two fields to find Route ID
    flight_origin = StringField('Origin', validators=[DataRequired()])
    flight_destination = StringField('Destination', validators=[DataRequired()])
    flight_number = IntegerField('Flight #', validators=[DataRequired()])
    weather_description = StringField('Weather Description', validators=[DataRequired()])
    aircraft_model = StringField('Aircraft Model', validators=[DataRequired()])
    airline_name = StringField('Airline Name', validators=[DataRequired()])
    price = IntegerField('Price ($)', validators=[DataRequired()])
    submit = SubmitField('Submit Flight')


