from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, PasswordField, SelectField, BooleanField, TextAreaField, FileField
from wtforms.fields.html5 import DateField
from wtforms.validators  import (DataRequired, Length, Optional, EqualTo, InputRequired, Regexp)
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.widgets import TextArea
from .models import db, Doctor, Department, Insurance, SurgeryProcedure, Patient, Side, PostopProcedure
from sqlalchemy.sql.expression import func
from flask_sqlalchemy import SQLAlchemy
from flask import session
from datetime import datetime


class SignupForm(FlaskForm):
    """Doctor Sign-up Form."""
    title = StringField(
        'Title',
        validators=[DataRequired()]
    )
    first_name = StringField(
        'First Name',
        validators=[DataRequired()]
    )
    last_name = StringField(
        'Last Name',
        validators=[DataRequired()]
    )
    #id_department = StringField(
    #    'ID of your Dpt. (ask your admin)',
    #    validators=[DataRequired()]
    #)
    department = SelectField(
        "Department", choices=[(1,"General Surgery"),(2,"Trauma Surgery"), (3, "Gynaecology")],
       validators=[InputRequired()]
       )
    username = StringField(
        'Username - refer to your Department or contact us',
        validators=[DataRequired()]
    )
    
      
    submit = SubmitField('Apply to Register')

class LoginForm(FlaskForm):
    """User/Doctor Log-in Form."""
    username = StringField(
        'Username',
        validators=[
            DataRequired()
            
        ]
    )
    
    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )
    submit = SubmitField(
        'Log In')   



class PatientAddForm(FlaskForm):
    """Add  Patients Form."""
    first_name = StringField(
        'First Name',
        validators=[DataRequired()]
    )
    last_name = StringField(
        'Last Name',
        validators=[DataRequired()]
    )
    date_birth = DateField(
        'Date of Birth',
        validators=[DataRequired()]
    )

    gender = SelectField(
        "Gender", choices=[("male","Male"),("female","Female"), ("divers", "Diverse")],
       validators=[InputRequired()]
       )
    
    #The following works but can be automated with databse queries!
    #id_insurance = SelectField(
    #    "Insurance", choices=[(1,"Barmer"),(2,"DAK Gesundheit"), (3, "Techniker Krankenkasse"), (4, "AOK Bayern"), (5, "Barmenia"),
    #                           (6, "Ottonova Health"), (7, "Selbstzahler"), (8, "DBK"), (9, "Hanseatische Krankenkasse"), (10, "IKK classic")],
    #   validators=[InputRequired()]
    #   )
    id_insurance=QuerySelectField('Insurance',query_factory=lambda:Insurance.query.order_by(Insurance.name),get_label="name")
   
    
      
    submit = SubmitField('Add new patient')

    



class InsuranceAddForm(FlaskForm):
    """Add Insurnaces Form."""
    
    id_insurance=QuerySelectField('Here you can check again whether Insurance is already in the system',query_factory=lambda:Insurance.query.order_by(Insurance.name),get_label="name", allow_blank = True)
   
    name = StringField(
        'Enter a new Insurance',
        validators=[
            DataRequired()])
    
      
    submit = SubmitField('Add Insurance')


class SurgProcAddForm(FlaskForm):
    """Surgical Procedures Add Form."""
    
    #typical_dpt_id=QuerySelectField('Insurance',query_factory=lambda:Insurance.query.order_by(Insurance.name),get_label="name")

    snomed_code = StringField(
        'Enter SNOMED Code Procedure',
        validators=[
            Regexp(regex ="^[0-9]*$")])
   
    name = StringField(
        'Enter the Name of your new Procedure',
        validators=[
            DataRequired()])
    
      
    submit = SubmitField('Add Surgical Procedure')
    

class NullableDateField(DateField):
    """Native WTForms DateField throws error for empty dates.
    Let's fix this so that we could have DateField nullable."""
    def process_formdata(self, valuelist):
        if valuelist:
            date_str = ' '.join(valuelist).strip()
            if date_str == '':
                self.data = None
                return
            try:
                self.data = datetime.datetime.strptime(date_str, self.format).date()
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('Not a valid date value'))

class OpTakenPlaceSearchForm(FlaskForm):
    """Search Mask"""

    search_name=StringField('If known, put in the last name of the Patient')

    search_date=StringField('Alternatively, try to search for the birthday here',
                            validators=[Regexp(regex ="^[0-9\-]*$")])
   
      
    submit = SubmitField('Proceed')

  
class OpTakenPlaceAddForm(FlaskForm):
    """Operations Taken Place Form."""

    last_name = QuerySelectField('Choose your Patient', get_label="searchname", allow_blank = False)

    snomed_code = QuerySelectField('Select the performed Surgical Procedure. Only Procedures of your department are displayed here.', query_factory=lambda:SurgeryProcedure.query.filter_by(typical_dpt_id = session["id_dep"][0]).order_by(SurgeryProcedure.name), get_label="name", allow_blank = False)
   
    id_side = QuerySelectField('Which side was operated on?', query_factory=lambda:Side.query, get_label="name_side", allow_blank = False)

    
    
      
    submit = SubmitField('Proceed')



class WHOChecklistForm(FlaskForm):
    """Boolean Form implementing the WHO Security Checklist."""
    ###BEFORE the surgery ####

    ident = BooleanField("Has the patient confirmed his/her identity, site, procedure, and consent?")

    marked = SelectField("Is the operation site marked?", choices=[("Yes","Yes"),("Not applicable","Not applicable")], validators=[InputRequired()])

    medcheck = BooleanField("Is the anaesthesia machine and medication check complete?")

    pulsoxy = BooleanField("Is the pulse oximeter on the patient and functioning?")

    allergy = SelectField("Does the patient have a known allergy?", choices=[("No","No"),("Yes","Yes")], validators=[InputRequired()])

    diffairway =  SelectField("Does the patient have a difficult airway or aspiration risk?", choices=[("No","No"),("Yes","Yes, and equipment/assistance available")], validators=[InputRequired()])

    riskblood = SelectField("Does the patient have a risk of >500ml blood loss (7ml/kg in children)?", choices=[("No","No"),("Yes","Yes, and two IVs/central access and fluids planned")], validators=[InputRequired()])

    ###During surgery###
    intro = BooleanField("Confirm all team members have introduced themselves by name and role.")

    patient = BooleanField("Confirm the patient’s name, procedure, and where the incision will be made.")

    antibiot = SelectField("Has antibiotic prophylaxis been given within the last 60 minutes?", choices=[("Not applicable","Not applicable"),("Yes","Yes")], validators=[InputRequired()])

                #Questions to surgeon:
    steps = BooleanField("What are the critical or non-routine steps?")

    time = BooleanField("How long will the case take?")

    bloodloss = BooleanField("What is the anticipated bloodloss?")

                #Questions to anaesthesist:
    speccons = BooleanField("Anaesthesiologist: \n Are there any patient-specific concerns?")

                #Questions to nurse team: 

    sterile = BooleanField("Nursing Team: \n Has sterility (including indicator results) been confirmed?")

    equipment = BooleanField("Nursing Team: \n Are there equipment issues or any concerns?")

    imaging = BooleanField("Is essential imaging displayed? Also check if not applicable.")


    ###Before patient leaves operating room###

                #Nur confirms verbally#

    procname = BooleanField("The name of the procedure")

    instruments = BooleanField("Completion of instrument, sponge and needle counts")

    specimen = BooleanField("Specimen labelling (read specimen labels aloud, including patient name)")

    equipment1 = BooleanField("Whether there are any equipment problems to be addressed")


    # Among surgeon, anesthesist and nurse:

    concerns = BooleanField("What are the key concerns for recovery and management of this patient?")





          
    submit = SubmitField('Proceed to post-OP documentation')



class PostOpDocForm(FlaskForm):
    """Operations Taken Place Form."""

    outcome = QuerySelectField('What was the outcome of the Surgery? Where was the patient transferred to?', query_factory=lambda:PostopProcedure.query.order_by(PostopProcedure.id_outcome.desc()),get_label="outcome", allow_blank = False)

    comment = TextAreaField('If you want you can already write your Surgery comment or report now. You can also do that anytime later.', widget = TextArea())

    date = DateField('What day was the surgery finished?', 
        validators=[DataRequired()]    )
    
      
    submit = SubmitField('Add surgery')


class AddPicForm(FlaskForm):
    """Operations Taken Place Form."""

    image = FileField("You can upload additional pictures of your surgery here")
   
      
    submit = SubmitField('Add picture')



