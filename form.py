from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import DateField

class RegistrationForm(FlaskForm):
    phonenumber = StringField('Phone Number',
                           validators=[DataRequired(), Length(min=2, max=20)])

    password = PasswordField('Password', validators=[DataRequired()])
    #confirm_password = PasswordField('Confirm Password',
                                     #validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    phonenumber = StringField('Phone Number', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class AddFoodForm(FlaskForm):
    name = StringField('Phone Number', validators=[DataRequired(), Length(min=2, max=20)])
    date = DateField('Expiration Date')
    submit = SubmitField('Add')

class DeleteFoodForm(FlaskForm):
    name = StringField('Phone Number', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Delete')