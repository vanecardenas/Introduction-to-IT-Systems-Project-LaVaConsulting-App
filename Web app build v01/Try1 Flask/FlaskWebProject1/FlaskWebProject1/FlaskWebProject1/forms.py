from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, PasswordField, SelectField
from wtforms.validators  import (DataRequired, Length, Optional, EqualTo, InputRequired)


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
        'Username',
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
    
  