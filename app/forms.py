from flask.ext.wtf import Form
from wtforms import (StringField, TextAreaField, BooleanField,
    SelectField, SubmitField)
from wtforms.validators import DataRequired


class BusinessForm(Form):
    city = SelectField('What city would you like to start your business in?', validators=[DataRequired()],
                       choices=[('nev', 'Nevada'), ('phil', 'Philidephia')])
    business = SelectField("What Business would you like to start?", validators=[DataRequired()],
                           choices=[('it', 'Italian'), ('thai', 'Thai')])
    submit = SubmitField("Find my businesses")