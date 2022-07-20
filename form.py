from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    phonenumber = StringField('Phone Number',
                           validators=[DataRequired(), Length(min=2, max=20)])

    password = PasswordField('Password', validators=[DataRequired()])
    #confirm_password = PasswordField('Confirm Password',
                                     #validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')