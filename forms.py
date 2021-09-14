from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Brugernavn', validators=[DataRequired(message="Feltet skal udfyldes"), Length(min=2, max=20, message="Skal være mellem 2 og 20 tegn")])
    email = StringField('Email', validators=[DataRequired(message="Feltet skal udfyldes"), Email(message="Ugyldig Email")])
    password = PasswordField('Kodeord', validators=[DataRequired(message="Feltet skal udfyldes")])
    confirm_password = PasswordField('Gentag kodeord', validators=[DataRequired(message="Feltet skal udfyldes"), EqualTo('password', message="Skal være identisk med kodeord")])
    submit = SubmitField('Opret konto')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message="Feltet skal udfyldes"), Email(message="Ugyldig Email")])
    password = PasswordField('Kodeord', validators=[DataRequired(message="Feltet skal udfyldes")])
    remember = BooleanField('Husk Mig')
    submit = SubmitField('Login')
