from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from .forms import LoginForm, SignupForm
from .models import db, Doctor
from . import login_manager
from FlaskWebProject1 import app
from flask_login import current_user, login_required



#Authentification page: right now initial page. Is handled here instead of in views.py. 


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Log-in page for registered users.

    GET requests serve Log-in page.
    POST requests validate and redirect user to dashboard.
    """
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('exploring_page'))

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        doctor = Doctor.query.filter_by(username=form.username.data).first()
        session["title"]=  db.session.query(Doctor.title).filter_by(username=form.username.data).first()
        session["last_name"]=  db.session.query(Doctor.last_name).filter_by(username=form.username.data).first()
        session["id_dep"]=  db.session.query(Doctor.id_department).filter_by(username=form.username.data).first()
        session["id_doc"]=  db.session.query(Doctor.id_doctor).filter_by(username=form.username.data).first()
        if doctor and doctor.check_password(password=form.password.data):
            login_user(doctor)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('exploring_page'))
        flash('Invalid username/password combination')
        return redirect(url_for('login'))
    return render_template(
        'login.html',
          form=form)


from flask_login import logout_user



@app.route("/logout")
@login_required
def logout():
    """User log-out."""
    logout_user()
    return redirect(url_for('initial_page'))