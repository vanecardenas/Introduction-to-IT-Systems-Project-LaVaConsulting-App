"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect, request, session, url_for
from FlaskWebProject1 import app
from flask_login import current_user, login_required 
#from .forms import LoginForm

@app.route('/', methods=('GET', 'POST'))
@app.route('/initial_page',  methods=('GET', 'POST'))
def initial_page():
   # form = LoginForm()
   # if form.validate_on_submit():
     #   return redirect(url_for("explanatory_page"))
    """Renders the home page."""
    return render_template(
        'initial_page.html',
        #form=form,
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
@login_required
def contact():
    
    """Renders the contact page."""
    return render_template(
        'contact_page.html',
        current_user=current_user,
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/logout_contact')
def logout_contact():
    """Renders the logged out contact page."""
    return render_template(
        'logout_contact_page.html',
        title='Contact us',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/about')
@login_required
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        current_user=current_user,
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/logout_about')
def logout_about():
    """Renders the about page."""
    return render_template(
        'logout_about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/add_new')
@login_required
def add_new():
    """Renders the addnew page."""
    return render_template(
        'add_new.html',
        current_user=current_user,
        title='Add New Surgery/Patient',
        year=datetime.now().year,
    )



@app.route('/impressum')
@login_required
def impressum():
    """Renders the disclaimer page."""
    return render_template(
        'impressum.html',
        current_user=current_user,
        title='Disclaimer',
        year=datetime.now().year,
    )

@app.route('/logout_impressum')
def logout_impressum():
    """Renders the logged out impressum page."""
    return render_template(
        'logout_impressum.html',
        title='Disclaimer',
        year=datetime.now().year,
        message='Your application description page.'
    )



@app.route('/user_dpt')
@login_required
def user_dpt():
    """Renders the department page."""
    return render_template(
        'user_dpt.html',
        current_user=current_user,
        title='User Department',
        year=datetime.now().year,
    )



@app.route('/user_patients')
@login_required
def user_patients():
    """Renders the My Patients page."""
    return render_template(
        'user_patients.html',
        current_user=current_user,
        title='My Patients',
        year=datetime.now().year,
    )



@app.route('/user_surgeries')
@login_required
def user_surgeries():
    """Renders the My Surgerires page."""
    return render_template(
        'user_surgeries.html',
        current_user=current_user,
        title='My Surgeries',
        year=datetime.now().year,
    )





@app.route('/exploring_page')
@login_required
def exploring_page():

    """Renders the another page."""
    return render_template(
        'exploring_page.html',
        current_user=current_user,
        d_title = session["title"][0] ,
        doc_name = session["last_name"][0] ,
        year=datetime.now().year,
    )


