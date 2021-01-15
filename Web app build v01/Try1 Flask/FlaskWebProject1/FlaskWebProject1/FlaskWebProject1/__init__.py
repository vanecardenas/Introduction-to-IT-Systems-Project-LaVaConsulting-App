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

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)






# Using a production configuration
#app.config.from_object('config.ProdConfig')

# Using a development configuration
app.config.from_object('config.Config')

import FlaskWebProject1.models
import FlaskWebProject1.views
import FlaskWebProject1.dbase_conn





