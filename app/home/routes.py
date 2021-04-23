# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user

from jinja2 import TemplateNotFound
from app.home.forms import UpdateSettingsForm, DashboardForm
from app.base.models import User, Car, Ride
from app import db, login_manager


@blueprint.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    dashboard_form = DashboardForm(request.form)
    if 'book' in request.form:
        cartype = request.form['cartype']
        car = Car.query.filter_by(cartype=cartype, active='false').first()
        car.active = 'true'
        print(request.form['source'])
        print(request.form['destination'])
        print(car.active)
        ride = Ride(
                ride=car,
                source=request.form['source'],
                destination=request.form['destination'],
            )
        db.session.add(ride)
        db.session.commit()
        
    return render_template('dashboard.html', segment='dashboard', form=dashboard_form)


@blueprint.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    setting_form = UpdateSettingsForm(request.form)
            #print("Inside settings html")

    if 'saveall' in request.form:
        user = User.query.filter_by(username=current_user.username).first()
        if user:
            # print("Checking user")
            user.firstname = request.form['firstname']
            user.lastname = request.form['lastname']
            user.address = request.form['address']
            user.city = request.form['city']
            user.zip = request.form['zip']
            user.houseno = request.form['houseno']
            user.dob = request.form['dob']
            # user.gender = request.form['firstname']
            user.phonenumber = request.form['phonenumber']
            print(user.firstname)
            db.session.commit()
            print(current_user.city)

            # bob = User.query.filter_by(username=current_user.username).first()
            # print('printing teh saved value')
            # print(bob.firstname)  # {}
    return render_template('settings.html', form=setting_form)

# @blueprint.route('/<template>',methods=['GET', 'POST'])
# @login_required
# def route_template(template):

#     try:

#         if not template.endswith( '.html' ):
#             template += '.html'

#         if template == 'settings.html':
#             setting_form = UpdateSettingsForm(request.form)
#             #print("Inside settings html")

#             if 'saveall' in request.form:
#                 user = User.query.filter_by(username=current_user.username).first()
#                 if user:
#                     # print("Checking user")
#                     user.firstname = request.form['firstname']
#                     user.lastname = request.form['lastname']
#                     user.address = request.form['address']
#                     user.city = request.form['city']
#                     user.zip = request.form['zip']
#                     user.houseno = request.form['houseno']
#                     user.dob = request.form['dob']
#                     #user.gender = request.form['firstname']
#                     user.phonenumber = request.form['phonenumber']
#                     print(user.firstname)
#                     db.session.commit()
#                     print(current_user.city)

#                     # bob = User.query.filter_by(username=current_user.username).first()
#                     # print('printing teh saved value')
#                     # print(bob.firstname)  # {}
#             return render_template('settings.html', form=setting_form)

#         # Detect the current page
#         segment = get_segment( request )

#         # Serve the file (if exists) from app/templates/FILE.html
#         return render_template( template, segment=segment )


#     except TemplateNotFound:
#         return render_template('page-404.html'), 404

    # except:
    #     return render_template('page-500.html'), 500

#Helper - Extract current page name from request


def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'dashboard'

        return segment    

    except:
        return None

