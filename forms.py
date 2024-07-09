from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, IntegerField
from wtforms.validators import InputRequired, NumberRange

species_type = [
  'Dog',
  'Cat',
  'porcupine'
]

class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators=[InputRequired('Pet cannot be blank')])
    species = SelectField('Species', choices = [(spes, spes) for spes in species_type])
    photo_url = StringField('Pet Photo URL')
    age = IntegerField('Pet Age', validators=[NumberRange(min=0, max=30, message='Age must be between 0 and 30')])
    notes = StringField('Pet Notes')
