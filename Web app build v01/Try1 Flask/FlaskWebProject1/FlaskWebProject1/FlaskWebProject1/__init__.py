"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

# Using a production configuration
#app.config.from_object('config.ProdConfig')

# Using a development configuration
app.config.from_object('config.DevConfig')

import FlaskWebProject1.views
import FlaskWebProject1.dbase_conn
