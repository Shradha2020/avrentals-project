# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

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