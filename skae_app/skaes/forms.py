from wtforms import StringField, PasswordField, SubmitField, TextAreaField,EmailField, validators,HiddenField
from flask_wtf import FlaskForm

class SignupForm(FlaskForm):
    first_name = StringField('First Name', [validators.DataRequired(), validators.Length(min=2, max=20)])
    last_name = StringField('Last Name', [validators.DataRequired(), validators.Length(min=2, max=20)])
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=2, max=20)])
    bio = TextAreaField('Bio', [ validators.Length(min=2, max=140)])
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')

class EditAccountForm(FlaskForm):
    first_name = StringField('First Name', [validators.DataRequired(), validators.Length(min=2, max=20)])
    last_name = StringField('Last Name', [validators.DataRequired(), validators.Length(min=2, max=20)])
    username = HiddenField('Username', [validators.DataRequired(), validators.Length(min=2, max=20)])
    bio = TextAreaField('Bio', [validators.Length(min=2, max=140)])
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    submit = SubmitField('Update')