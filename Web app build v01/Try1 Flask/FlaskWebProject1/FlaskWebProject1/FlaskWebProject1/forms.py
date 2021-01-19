from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, PasswordField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators  import (DataRequired, Length, Optional, EqualTo, InputRequired)
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from .models import db, Doctor, Department, Insurance
from sqlalchemy.sql.expression import func
from flask_sqlalchemy import SQLAlchemy


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
    """User Log-in Form."""
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
    """Doctor Sign-up Form."""
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
    id_insurance=QuerySelectField('Insurance',query_factory=lambda:Insurance.query,get_label="name")
   
    
      
    submit = SubmitField('Add new patient')

    def edit_patient(request, id_insurance):
        insurance = Insurance.objects.get(pk=id_insurance)
        form = PatientAddForm(obj=article)
        form.id_insurance.queryset = Insurance.objects.filter(author=request.user)
    
  