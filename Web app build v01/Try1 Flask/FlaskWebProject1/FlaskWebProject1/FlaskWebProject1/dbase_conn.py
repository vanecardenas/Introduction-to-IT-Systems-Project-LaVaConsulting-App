#THis file is currently not needed but was used to try out a lot of databse stuff. Future routes could be stored here. 

from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
import flask_sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table
import pymysql
import mysql.connector
from mysql.connector import Error
import cx_Oracle
#import sqlacodegen

#What we should do in an ideal world: connect to sqlalchemy, read out the database using sqlacodegen and then use flask-sqlalchemy to do all the magic 

#flask-sqlacodegen "mysql://root:vanessa@127.0.0.1/surgeries_db" --outfile "models.py"

from FlaskWebProject1 import app
app.config.from_object('config.Config')

db = SQLAlchemy(app)
from FlaskWebProject1.models import Department

#db.session.query(Department).filter(Department.id_department==1).all() works


@app.route('/test_db')
def test1():
    try:
            test = db.session.query(Department).all()
            print(test) #Look in console to see if database connection works
               
        
            return '<h1>Database connection succesful!</h1>'
    except:
        return '<h1>Database connection not correctly established!</h1>'























cnx = mysql.connector.connect(
             host="127.0.0.1",
             port=3306,
             user = "root",
             password = "vanessa",
             autocommit = True
            )


@app.route('/test_1')
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


#@app.route('/test_db')
#def test1():
#    try:
#            engine = db.create_engine('mysql+pymsql//root:vanessa@127.0.0.1:3006/surgeries_db')
#            table1meta = MetaData(engine)
#            table1 = Table('doctors', table1meta, autoload=True)
#            DBSession = sessionmaker(bind=engine)
#            session = db.DBSession()
#            results = db.session.query(table1).filter(table1.columns.id_department=="1")
#            results.all().fetchall()
               
        
#            return '<h1>Database connection succesful!</h1>'
#    except:
#        return '<h1>Database connection not correctly established!</h1>'
        


#app.config['MYSQL_HOST'] = '127.0.0.1'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'vanessa'
#app.config['MYSQL_DB'] = 'surgery_db'

#mysql = MySQL(app)