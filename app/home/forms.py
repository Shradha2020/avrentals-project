# -*- encoding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField , SubmitField, SelectField
from wtforms.validators import InputRequired, Email, DataRequired

## Settings

class UpdateSettingsForm(FlaskForm):
    firstname = TextField('firstname'     , id='firstname_create')
    lastname = TextField('lastname'     , id='last_create')
    phonenumber = TextField('phonenumber'     , id='phonenumber_create')
    dob = TextField('dob'     , id='dob')
    gender = SelectField('gender'     , id='gender', choices=[('', 'Select Gender'), ('female', 'Female'), ('male', 'Male')])
    city = TextField('city'     , id='city')
    zip = TextField('zip'     , id='zip')
    address = TextField('address'     , id='address')
    houseno = TextField('houseno', id='houseno')
    saveall = SubmitField('saveall')

class DashboardForm(FlaskForm):
    source = TextField('source', id='source')
    destination = TextField('destination', id='destination')
    cartype = SelectField('cartype', id='cartype', choices=[('', 'View car types'), ('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Limousine', 'Limousine')])
    book = SubmitField('book')