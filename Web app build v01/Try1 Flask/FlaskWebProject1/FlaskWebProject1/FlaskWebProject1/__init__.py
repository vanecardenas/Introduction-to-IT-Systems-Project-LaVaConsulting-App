"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
import mysql.connector



app = Flask(__name__)

# Using a production configuration
#app.config.from_object('config.ProdConfig')

# Using a development configuration
app.config.from_object('config.Config')

import FlaskWebProject1.views
import FlaskWebProject1.dbase_conn




