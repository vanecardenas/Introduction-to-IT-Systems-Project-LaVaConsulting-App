from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from .forms import PatientAddForm
from .models import db, Doctor, Department, Patient, Insurance
from . import login_manager
from FlaskWebProject1 import app
from flask_login import current_user, login_required
from sqlalchemy.sql.expression import func
from datetime import datetime


#Authentification page: This is the module for all funcionality related to adding patients and procedures to the database. For signing up and adding a user see auth.py.



@app.route('/add_new')
@login_required
def add_new():
    
    """Renders the addnew page."""
    return render_template(
        'add_new.html',
        current_user=current_user,
        doc_dept =   session["depname"][0],
        d_title = session["title"][0] ,
        doc_name = session["last_name"][0],
        title='Add New Surgery/Patient',
        add_message ="",
        year=datetime.now().year    ) 

def reset_cookie():

    time.sleep(3)
    session["add_message"] = ""










@app.route('/addpatient', methods=['GET', 'POST'])
@login_required
def addpatient():
    """
    Page for adding a user.

      """
    form = PatientAddForm()
    
    if form.validate_on_submit():
            
            #pid = db.session.query(func.max(Patient.id_patient)).scalar() +1
            new_patient = Patient(
                #id_patient = pid,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                date_birth=form.date_birth.data,
                gender= form.gender.data,
                id_insurance= form.id_insurance.data.id_insurance
            )
            
            db.session.add(new_patient)
            db.session.commit() 
            #session["add_message"]=  "Patient successfully added!"

           # Create new user
            # Log in as newly created user
            flash('Patient was successfully added!')
            return redirect(url_for('add_new', add_message= "Patient successfully added!",**request.args))
        
    return render_template(
        'add_patient.html',
        title='Create an Account.',
        form=form,
        template='signup-page',
        body="Sign up for a user account."
    )
