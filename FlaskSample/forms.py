from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional

class AddPlayerForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    position = StringField("Position", validators=[DataRequired()])
    bat_order = IntegerField("Batting Order", validators=[DataRequired(), NumberRange(min=1)])
    at_bats = IntegerField("At Bats", validators=[Optional()])
    hits = IntegerField("Hits", validators=[Optional()])
    submit = SubmitField("Add Player")

class UpdatePlayerForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    position = StringField("Position", validators=[DataRequired()])
    bat_order = IntegerField("Batting Order", validators=[DataRequired(), NumberRange(min=1)])
    at_bats = IntegerField("At Bats", validators=[Optional()])
    hits = IntegerField("Hits", validators=[Optional()])
    submit = SubmitField("Update Player")
