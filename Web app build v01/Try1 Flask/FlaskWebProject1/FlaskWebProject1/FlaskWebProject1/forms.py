from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, PasswordField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators  import (DataRequired, Length, Optional, EqualTo, InputRequired, Regexp)
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from .models import db, Doctor, Department, Insurance, SurgeryProcedure, Patient, Side
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
        "Gender", choices=[("male","Male"),("female","Female")],
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
    
    id_insurance=QuerySelectField('Here you can check again whether Insurance is in the system',query_factory=lambda:Insurance.query.order_by(Insurance.name),get_label="name", allow_blank = True)
   
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
    """Operations Taken Place Form."""

    search_name=StringField('If known, put in the last name of the Patient')

    search_date=StringField('Alternatively, try to search for the birthday here',
                            validators=[Regexp(regex ="^[0-9\-]*$")])
   
      
    submit = SubmitField('Proceed')

  
class OpTakenPlaceAddForm(FlaskForm):
    """Operations Taken Place Form."""

    last_name=QuerySelectField('Choose your Patient', get_label="searchname", allow_blank = False)

    snomed_code=QuerySelectField('Select the performed Surgical Procedure. Only Procedures of your department are displayed here.', query_factory=lambda:SurgeryProcedure.query.filter_by(typical_dpt_id = session["id_dep"][0]).order_by(SurgeryProcedure.name), get_label="name", allow_blank = False)
   
    id_side=QuerySelectField('Which side was operated on?', query_factory=lambda:Side.query.order_by(Side.id_side), get_label="name_side", allow_blank = False)
    
      
    submit = SubmitField('Proceed')


