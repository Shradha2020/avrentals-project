# -*- encoding: utf-8 -*-

from app.home import blueprint
from flask import render_template, redirect, url_for, request, session , send_file
from flask_login import login_required, current_user

from jinja2 import TemplateNotFound
from app.home.forms import UpdateSettingsForm, DashboardForm
from app.base.models import User, Car, Ride
from app import db, login_manager
import os
import random
# from app.home.s3_demo import list_files, download_file, upload_file


UPLOAD_FOLDER = "uploads"
BUCKET = "trailcloudupload"

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
        ride = Ride(
                ride=car,
                source=request.form['source'],
                destination=request.form['destination'],
            )
        db.session.add(ride)
        db.session.commit()
        return render_template('dashboard.html', segment='dashboard', form=dashboard_form, car=car)
    else:    
        return render_template('dashboard.html', segment='dashboard', form=dashboard_form)


@blueprint.route('/dashboard-admin', methods=['GET', 'POST'])
@login_required
def dashboardadmin():
    data = Car.query.all()  # data from database
    page = request.args.get('page', 1, type=int)

    user_data = User.query.paginate(page=page, per_page=5)

    random_no = []
    for row in data:
        random_no.append(random.randint(50, 100))
    print(random_no)
    return render_template('dashboard-admin.html', query=data, user_query=user_data, battery=random_no, zip=zip)


@blueprint.route('/dashboard-owner', methods=['GET', 'POST'])
@login_required
def dashboardowner():
        data = Car.query.filter_by(user_id = current_user.id ).all()  # data from database
        carrides_owned = []
        # page = request.args.get('page', 1, type=int)
        for i in data:
            rides = Ride.query.filter_by(car_id=i.id).all()
            carrides_owned.extend(rides)
        return render_template('dashboard-owner.html', query=data, carrides=carrides_owned)


@blueprint.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    setting_form = UpdateSettingsForm(request.form)
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
            user.gender = request.form['gender']
            user.phonenumber = request.form['phonenumber']
            print(user.gender)
            db.session.commit()

    return render_template('settings.html', form=setting_form)

@blueprint.route('/transactions', methods=['GET', 'POST'])
@login_required
def transactions():
    # data = Car.query.all()  # data from database
    # user_data = User.query.all()
    return render_template('transactions.html')

# @blueprint.route('/storage')
# @login_required
# def storage():
#     print("hello")
#     #contents = list_files("avcloudbucket")
#     contents = list_files("trailcloudupload")
#     return render_template('storage.html', segment='index' , contents=contents)

# @blueprint.route("/upload", methods=['POST'])
# def upload():
#     if request.method == "POST":
#         f = request.files['file']
#         f.save(os.path.join(UPLOAD_FOLDER, f.filename))
#         upload_file(f"{f.filename}", BUCKET)

#         return redirect({{ url_for('home_blueprint.storage') }})

# @blueprint.route("/download/<filename>", methods=['GET'])
# def download(filename):
#     if request.method == 'GET':
#         output = download_file(filename, BUCKET)

#         return send_file(output, as_attachment=True)


# @blueprint.route('/<template>',methods=['GET', 'POST'])
# @login_required
# def route_template(template):
#
#     try:
#
#         if not template.endswith( '.html' ):
#             template += '.html'
#
#         if template == 'storage.html':
#             print('hello')
#             contents = list_files("avcloudbucket")
#             return render_template('storage.html', segment='index', contents=contents)
#
#
#         if template == 'settings.html':
#             setting_form = UpdateSettingsForm(request.form)
# >>>>>>> Stashed changes
#             #print("Inside settings html")
#
#     if 'saveall' in request.form:
#         user = User.query.filter_by(username=current_user.username).first()
#         if user:
#             # print("Checking user")
#             user.firstname = request.form['firstname']
#             user.lastname = request.form['lastname']
#             user.address = request.form['address']
#             user.city = request.form['city']
#             user.zip = request.form['zip']
#             user.houseno = request.form['houseno']
#             user.dob = request.form['dob']
#             # user.gender = request.form['firstname']
#             user.phonenumber = request.form['phonenumber']
#             print(user.firstname)
#             db.session.commit()
#             print(current_user.city)
#
#             # bob = User.query.filter_by(username=current_user.username).first()
#             # print('printing teh saved value')
#             # print(bob.firstname)  # {}
#     return render_template('settings.html', form=setting_form)
#
# def get_segment( request ):
#
#     try:
#
#         segment = request.path.split('/')[-1]
#
#         if segment == '':
#             segment = 'dashboard'
#
#         return segment
#
#     except:
#         return None

