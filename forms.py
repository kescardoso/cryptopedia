# Code used from tutorial:
# Python Flask Tutorial: Full-Featured Web App Part 3 - Forms and User Input
# https://www.youtube.com/watch?v=UIJKdCIEXUQ&t=23s

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo


# User Registration Form
class RegistrationForm(FlaskForm):
    # Username Field/Label
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    # Email Field/Label
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    # Password Field/Label
    password = PasswordField('Pasword', 
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Pasword', 
                                     validators=[DataRequired(), EqualTo('password')])
    # Submit Button
    submit = SubmitField('Sign Up')


# User Login Form
class LoginForm(FlaskForm):
    # Email Field/Label
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    # Password Field/Label
    password = PasswordField('Pasword', 
                             validators=[DataRequired()])
    # Remember Cookie Session
    remember = BooleanField('Remember me')
    # Submit Button
    submit = SubmitField('Login')
    
