"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
import mysql.connector
from config import Config
from flask_migrate import Migrate
from sqlalchemy.dialects.mysql import LONGBLOB, LONGTEXT
from flask_login import LoginManager
from flask import redirect, render_template, flash, request, session, url_for


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.init_app(app)

from .models import db, Doctor


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return Doctor.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('login'))




# Using a production configuration
#app.config.from_object('config.ProdConfig')

# Using a development configuration
app.config.from_object('config.Config')

import FlaskWebProject1.models
import FlaskWebProject1.forms
import FlaskWebProject1.views
import FlaskWebProject1.auth
import FlaskWebProject1.dbase_conn





