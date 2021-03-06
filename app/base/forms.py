# -*- encoding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, DataRequired

## login and registration

class LoginForm(FlaskForm):
    username = TextField    ('Username', id='username_login'   , validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login'        , validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
    username = TextField('Username'     , id='username_create' , validators=[DataRequired()])
    email    = TextField('Email'        , id='email_create'    , validators=[DataRequired(), Email()])
    password = PasswordField('Password' , id='pwd_create'      , validators=[DataRequired()])
    role     = SelectField('Role'       , id='role'            , validators=[DataRequired()], choices=[('', 'View roles'), ('owner', 'Car owner'), ('user', 'Car user'), ('admin', 'System administrator')], render_kw={'onchange': 'enable_fn()'})
    carmodel = TextField('carmodel'     , id='carmodel'        , validators=[DataRequired()], render_kw={'disabled':'True'})
    carNo = TextField('carNo' , id='carNo', validators=[DataRequired()], render_kw={'disabled':'True'})
    carcolor = TextField('carcolor' , id='carcolor', validators=[DataRequired()], render_kw={'disabled':'True'})
    cartype = SelectField('cartype', id='cartype', choices=[('', 'View car types'), ('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Limousine', 'Limousine')], render_kw={'disabled':'True'})
