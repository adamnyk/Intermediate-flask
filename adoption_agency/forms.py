from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, URL, Optional, AnyOf, NumberRange

ACCEPTED_PET_SPECIES = ["dog", "cat", "hedgehog"]

class PetForm(FlaskForm):
    name = StringField("Pet name", validators=[
        InputRequired(message="Name cannot be blank")])
    # species = StringField("Species", validators=[
    #     InputRequired(message="Name cannot be blank"), AnyOf(values=ACCEPTED_PET_SPECIES, message="We are only accepting the following species: %(values)s")])
    species = SelectField("Species,", choices= [(pet, pet) for pet in ACCEPTED_PET_SPECIES])
    img_url = StringField("Photo URL", validators=[
        Optional(),URL(require_tld=True, message='Invalid URL.')
        ])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="We are only accepting pets between %(min)s and %(max)s years old")])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    img_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Notes",
        validators=[Optional()],
    )

    available = BooleanField("Available?")
