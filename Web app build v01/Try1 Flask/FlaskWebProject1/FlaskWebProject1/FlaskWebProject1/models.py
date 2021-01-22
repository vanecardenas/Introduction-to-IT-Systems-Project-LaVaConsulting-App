# coding: utf-8
import sqlalchemy
from sqlalchemy.sql import func
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, column_property
from sqlalchemy.dialects.mysql import LONGBLOB, LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, redirect
from config import Config
from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from FlaskWebProject1 import app
from FlaskWebProject1 import db


#Base = declarative_base()
#metadata = Base.metadata

#app = Flask(__name__)
#app.config.from_object(Config)
#db = SQLAlchemy(app)

class Department(db.Model):
    __tablename__ = 'departments'

    id_department = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(45))
    contact_person = db.Column(db.String(45))

    def __repr__(self):
        return '<Department %r>' % self.department_name

class Insurance(db.Model):
    __tablename__ = 'insurances'

    id_insurance = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))


    def __repr__(self):
        return '<Insurance %r>' % self.name


class PostopProcedure(db.Model):
    __tablename__ = 'postop_procedure'

    id_outcome = db.Column(db.Integer, primary_key=True, unique=True)
    outcome = db.Column(db.String(45))

    def __repr__(self):
        return '<PostopProcedure %r>' % self.outcome


class Side(db.Model):
    __tablename__ = 'sides'

    id_side = db.Column(db.Integer, primary_key=True)
    name_side = db.Column(db.String(45))

    def __repr__(self):
        return '<Side %r>' % self.namde.side


class Doctor(UserMixin, db.Model):
    __tablename__ = 'doctors'
    __table_args__ = {'comment': 'List of operating doctors '}

    id_doctor = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45))
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    id_department = db.Column(db.ForeignKey('departments.id_department'), index=True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(200),
        primary_key=False,
        unique=False,
        nullable=False)

    department = db.relationship('Department')
    def get_id(self):
           return (self.id_doctor)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)



    def __repr__(self):
        return '<Doctor %r>' % self.last_name


class Patient(db.Model):
    __tablename__ = 'patients'
    __table_args__ = {'comment': 'Data characterizing the patient '}

    id_patient = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    date_birth = db.Column(db.Date)
    gender = db.Column(db.String(45))
    id_insurance = db.Column(db.ForeignKey('insurances.id_insurance'), index=True)
    searchname= column_property(last_name +", "+ first_name)
                               #", *" + (date_birth).strftime
                               

    insurance = db.relationship('Insurance')
    def __repr__(self):
        return '<Patient %r>' % self.last_name


class SurgeryProcedure(db.Model):
    __tablename__ = 'surgery_procedures'

    snomed_code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    typical_dpt_id = db.Column(db.ForeignKey('departments.id_department'), index=True)

    typical_dpt = db.relationship('Department')

    def __repr__(self):
        return '<SuergeryProcedure %r>' % self.name


class OperationsTakenPlace(db.Model):
    __tablename__ = 'operations_taken_place'

    id_operation = db.Column(db.Integer, primary_key=True)
    id_patient = db.Column(db.ForeignKey('patients.id_patient'), index=True)
    snomed_code = db.Column(db.ForeignKey('surgery_procedures.snomed_code'), index=True)
    id_side = db.Column(db.ForeignKey('sides.id_side'), index=True)
    id_doctor = db.Column(db.ForeignKey('doctors.id_doctor'), index=True)
    date = db.Column(db.Date)
    check_list = db.Column(db.Integer)
    id_outcome = db.Column(db.ForeignKey('postop_procedure.id_outcome'), index=True)
    comments = db.Column(sqlalchemy.dialects.mysql.LONGTEXT)
    pictures = db.Column(sqlalchemy.dialects.mysql.LONGBLOB)

    doctor = db.relationship('Doctor')
    postop_procedure = db.relationship('PostopProcedure')
    patient = db.relationship('Patient')
    side = db.relationship('Side')
    surgery_procedure = db.relationship('SurgeryProcedure')
    def __repr__(self):
        return '<OperationsTakenPlace %r>' % self.id_operation
