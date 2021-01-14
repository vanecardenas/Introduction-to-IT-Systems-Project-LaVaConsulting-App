from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
import flask_sqlalchemy

import mysql.connector
from mysql.connector import Error
import cx_Oracle

from FlaskWebProject1 import app
app.config.from_object('config.Config')

cnx = mysql.connector.connect(
             host="127.0.0.1",
             port=3306,
             user = "root",
             password = "vanessa",
             autocommit = True
            )

db = SQLAlchemy(app)

@app.route('/test_db')
def testdb():
    try:
          #Get a cursor
        cursor = cnx.cursor()

        def run_query(query, fetch = True): 
             # Execute a query
                cursor.execute(query)
                if fetch:
                # Fetch all results
                    records = cursor.fetchall()
                    return records        
        t_db= run_query('Show databases')
        return '<h1>Database connection succesful!</h1>'
    except:
        return '<h1>Database connection not correctly established!</h1>'
        


#app.config['MYSQL_HOST'] = '127.0.0.1'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'vanessa'
#app.config['MYSQL_DB'] = 'surgery_db'

#mysql = MySQL(app)