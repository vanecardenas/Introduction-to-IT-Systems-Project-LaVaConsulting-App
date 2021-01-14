"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
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
def contact():
    
    """Renders the contact page."""
    return render_template(
        'contact_page.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/add_new')
def add_new():
    """Renders the addnew page."""
    return render_template(
        'add_new.html',
        title='Add New Surgery/Patient',
        year=datetime.now().year,
    )



@app.route('/impressum')
def impressum():
    """Renders the disclaimer page."""
    return render_template(
        'impressum.html',
        title='Disclaimer',
        year=datetime.now().year,
    )



@app.route('/user_dpt')
def user_dpt():
    """Renders the department page."""
    return render_template(
        'user_dpt.html',
        title='User Department',
        year=datetime.now().year,
    )



@app.route('/user_patients')
def user_patients():
    """Renders the My Patients page."""
    return render_template(
        'user_patients.html',
        title='My Patients',
        year=datetime.now().year,
    )



@app.route('/user_surgeries')
def user_surgeries():
    """Renders the My Surgerires page."""
    return render_template(
        'user_surgeries.html',
        title='My Surgeries',
        year=datetime.now().year,
    )



@app.route('/exploring_page')
def exploring_page():
    """Renders the another page."""
    return render_template(
        'exploring_page.html',
        title='Home Page',
        year=datetime.now().year,
    )
