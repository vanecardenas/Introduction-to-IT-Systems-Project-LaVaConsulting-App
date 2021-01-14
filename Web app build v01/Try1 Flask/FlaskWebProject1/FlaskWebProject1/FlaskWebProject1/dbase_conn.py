from flask import Flask, render_template, request
from flask_mysqldb import MySQL


from FlaskWebProject1 import app

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'vanessa'
app.config['MYSQL_DB'] = 'surgery_db'

mysql = MySQL(app)