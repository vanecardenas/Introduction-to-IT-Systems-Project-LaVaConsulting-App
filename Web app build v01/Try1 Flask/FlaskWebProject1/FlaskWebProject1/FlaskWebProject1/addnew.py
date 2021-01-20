from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from .forms import PatientAddForm, InsuranceAddForm, SurgProcAddForm
from .models import db, Doctor, Department, Patient, Insurance, SurgeryProcedure
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










@app.route('/add_patient', methods=['GET', 'POST'])
@login_required
def add_patient():
    """
    Page for adding a user.

      """
    form = PatientAddForm()
    
    if form.validate_on_submit():
            
            pid = db.session.query(func.max(Patient.id_patient)).scalar() +1
            new_patient = Patient(
                id_patient = pid,
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
        current_user=current_user,
        doc_dept =   session["depname"][0],
        d_title = session["title"][0] ,
        doc_name = session["last_name"][0],
        title='Create an Account.',
        form=form,
        template='signup-page',
        body="Sign up for a user account."
    )



@app.route('/add_insurance', methods=['GET', 'POST'])
@login_required
def add_insurance():
    """
    Page for adding another insurance.

      """
    form = InsuranceAddForm()
    
    if form.validate_on_submit():
        existing_insurance = Insurance.query.filter_by(name=form.name.data).first()
        if existing_insurance is None:
             n_iid = db.session.query(func.max(Insurance.id_insurance)).scalar() +1
             new_insurance = Insurance(
                name=form.name.data,
                id_insurance = n_iid)
            
             db.session.add(new_insurance)
             db.session.commit() 

             flash('Insurance was successfully added!')
             return redirect(url_for('add_patient', add_message= "Insurance successfully added!",**request.args))
        flash('This insurance already exists!.')
        ...
        
    return render_template(
        'add_insurance.html',
        current_user=current_user,
        doc_dept =   session["depname"][0],
        d_title = session["title"][0] ,
        doc_name = session["last_name"][0],
        title='Create an Account.',
        form=form,
        template='Add insurance',
        body="Add another insurance."
    )


@app.route('/add_surgproc', methods=['GET', 'POST'])
@login_required
def add_surgproc():
    """
    Page for adding another surgical procedure.

      """
    form = SurgProcAddForm()
    
    if form.validate_on_submit():
        existing_insurance = SurgeryProcedure.query.filter_by(name=form.name.data).first()
        if existing_insurance is None:
             new_surgproc = SurgeryProcedure(
                name=form.name.data,
                snomed_code = form.snomed_code.data,
                typical_dpt_id =  session["id_dep"][0])
            
             db.session.add(new_surgproc)
             db.session.commit() 

             flash('Surgical Procedure was successfully added!')
             return redirect(url_for('add_new', add_message= "Surgical Procedure successfully added!",**request.args))
        flash('This Surgical Procedure already exists!.')
        ...
        
    return render_template(
        'add_surgproc.html',
        current_user=current_user,
        doc_dept =   session["depname"][0],
        d_title = session["title"][0] ,
        doc_name = session["last_name"][0],
        title='Create an Account.',
        form=form,
        template='Add insurance',
        body="Add another insurance."
    )


