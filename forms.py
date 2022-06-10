
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, url

numbers = range(31)

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired(message="Pet must have a name")])

    species = SelectField("Species", choices=[('Dog','Dog'),('Cat','Cat'),('Porcupine','Porcupine')], validators=[InputRequired(message="Pet must have a species")])

    photo_url = StringField("Photo URL", validators=[url(),Optional()])

    age = SelectField('Age', choices=[ (num,num) for num in numbers], coerce=int, validators=[Optional()])

    notes = StringField('Notes', validators=[Optional()])

    available = BooleanField("Is this pet available?", validators=[Optional()])
    

