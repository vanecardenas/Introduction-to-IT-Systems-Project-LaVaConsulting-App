from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from .forms import PatientAddForm, InsuranceAddForm, SurgProcAddForm, OpTakenPlaceAddForm, OpTakenPlaceSearchForm, WHOChecklistForm, PostOpDocForm, AddPicForm
from .models import db, Doctor, Department, Patient, Insurance, SurgeryProcedure, Side, OperationsTakenPlace
from . import login_manager
from FlaskWebProject1 import app
from flask_login import current_user, login_required
from sqlalchemy.sql.expression import func
from datetime import datetime
import werkzeug
from flask_uploads import configure_uploads, IMAGES, UploadSet
import base64
import base64image


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


@app.route('/add_optakenplace0', methods=['GET', 'POST'])
@login_required
def add_optakenplace0():
    """
    First Search Page for adding a surgery.

      """

    form = OpTakenPlaceSearchForm()

    if form.validate_on_submit():
        session["search_name"] = form.search_name.data
        session["search_date"] = form.search_date.data


        #flash('Surgical Procedure was successfully added!')
        return redirect(url_for('add_optakenplace1', add_message= "Surgical Procedure successfully added!",**request.args))
        
    
        
    return render_template(
        'add_op0.html',
        current_user=current_user,
        doc_dept =   session["depname"][0],
        d_title = session["title"][0] ,
        doc_name = session["last_name"][0],
        title='Create an Account.',
        form=form,
        template='Add insurance',
        body="Add another insurance."
    )


@app.route('/add_optakenplace1', methods=['GET', 'POST'])
@login_required
def add_optakenplace1():
    """
    Page for adding another surgical procedure.

      """

    form = OpTakenPlaceAddForm()

    form.last_name.query_factory=lambda:Patient.query.order_by(Patient.last_name)

    if session["search_name"] != "" and session["search_date"] == "":
        form.last_name.query_factory=lambda:Patient.query.filter_by(last_name= session["search_name"]).order_by(Patient.last_name)
        flash("Searched patients by name!")
        resnum  = Patient.query.filter_by(last_name= session["search_name"]).count()
        flash("Number of results: "+ str(resnum))
        

    if session["search_date"] != "":
        form.last_name.query_factory=lambda:Patient.query.filter_by(date_birth= session["search_date"]).order_by(Patient.last_name)
        flash("Searched patients by birthday!")
        resnum = Patient.query.filter_by(date_birth= session["search_date"]).count()
        flash("Number of results: "+ str(resnum))

    if session["search_date"] == "" and session["search_name"] == "" :

        flash("No input - all patients are shown!")

    if form.validate_on_submit():
        session["newop_patient_id"] = form.last_name.data.id_patient
        session["newop_snomed_code"] = form.snomed_code.data.snomed_code
        session["newop_id_side"] = form.id_side.data.id_side
        #session["op_date"] = form.date.data
        
        session.pop('_flashes', None)


        return redirect(url_for('add_optakenplace2', **request.args))
        
    
        
    return render_template(
        'add_op1.html',
        current_user=current_user,
        doc_dept =   session["depname"][0],
        d_title = session["title"][0] ,
        doc_name = session["last_name"][0],
        title='Create an Account.',
        form=form,
    )


@app.route('/add_optakenplace2', methods=['GET', 'POST'])
@login_required
def add_optakenplace2():
    """
    Page for checking the WHO checklist.

      """

    form = WHOChecklistForm()

    

    if form.validate_on_submit():
        if form.ident.data == True and form.medcheck.data == True and form.pulsoxy.data == True and form.intro.data == True and form.patient.data == True and form.steps.data == True \
            and form.time.data == True and form.bloodloss.data == True and form.speccons.data == True and form.sterile.data == True and form.equipment.data == True \
            and form.imaging.data == True and form.procname.data == True and form.instruments.data == True and form.specimen.data == True and form.equipment1.data == True \
            and form.concerns.data == True:

            session["state_checklist"] = "complete"
            flash("Checklist complete!")

        else:
            session["state_checklist"] = "incomplete"
            flash("Checklist was incomplete! This has been saved.")


        #This is the place where we can implement a saving of the checklist results. Could be saved to the database as a list maybe? Or as a dict? Need a new database column for this though.





        return redirect(url_for('add_optakenplace3', **request.args))
        
    
        
    return render_template(
        'add_op2.html',
        current_user=current_user,
        doc_dept =   session["depname"][0],
        d_title = session["title"][0] ,
        doc_name = session["last_name"][0],
        title='Create an Account.',
        form=form,
    )



images = UploadSet('images', IMAGES)
configure_uploads(app, images)

@app.route('/add_optakenplace3', methods=['GET', 'POST'])
@login_required
def add_optakenplace3():
    """
    Page for documenting the outcome, comments and possibly already pictures. Since the picture stuff is more complicated I might first try this on yet another page. The database commit will happen here though. 

      """

    form = PostOpDocForm()

    

    if form.validate_on_submit():

        #filename = images.save(form.image.data)
        #form.image.data.stream.seek(0)
        #image_string = base64.b64encode(form.image.data.read())


        id_surg = db.session.query(func.max(OperationsTakenPlace.id_operation)).scalar() +1
        session["curr_id_surg"] = id_surg

        new_surgery = OperationsTakenPlace(
            id_operation= id_surg,
            id_patient=  session["newop_patient_id"],
            snomed_code = session["newop_snomed_code"],
            id_side = session["newop_id_side"],
            id_doctor = session["id_doc"],
            date = form.date.data,
            check_list = session["state_checklist"],
            id_outcome= form.outcome.data.id_outcome,
            comments = form.comment.data,
            
           
            )

        db.session.add(new_surgery)
        db.session.commit()

        flash("Surgery was added!")




        return redirect(url_for('add_pic', **request.args))
        
    
        
    return render_template(
        'add_op3.html',
        current_user=current_user,
        doc_dept =   session["depname"][0],
        d_title = session["title"][0] ,
        doc_name = session["last_name"][0],
        title='Create an Account.',
        form=form,
    )


@app.route('/add_pic', methods=['GET', 'POST'])
@login_required
def add_pic():
    """
   Page for adding pictures 

      """

    form = AddPicForm()

    

    if form.validate_on_submit():

        filename = images.save(form.image.data)
        form.image.data.stream.seek(0)
        image_string = base64.b64encode(form.image.data.read())



        
        surgery = OperationsTakenPlace.query.get(session["curr_id_surg"])
        surgery.pictures = image_string

        
        db.session.update()

        flash("Picture was added!")
        session.pop("curr_id_surg")




        return redirect(url_for('add_new', **request.args))
        
    
        
    return render_template(
        'add_op4.html',
        current_user=current_user,
        doc_dept =   session["depname"][0],
        d_title = session["title"][0] ,
        doc_name = session["last_name"][0],
        title='Create an Account.',
        form=form,
    )
