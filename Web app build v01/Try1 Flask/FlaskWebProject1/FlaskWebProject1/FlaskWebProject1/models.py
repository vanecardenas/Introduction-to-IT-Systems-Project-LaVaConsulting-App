# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import LONGBLOB, LONGTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Department(Base):
    __tablename__ = 'departments'

    id_department = Column(Integer, primary_key=True)
    department_name = Column(String(45))
    contact_person = Column(String(45))


class Insurance(Base):
    __tablename__ = 'insurances'

    id_insurance = Column(Integer, primary_key=True)
    name = Column(String(45))


class PostopProcedure(Base):
    __tablename__ = 'postop_procedure'

    id_outcome = Column(Integer, primary_key=True, unique=True)
    outcome = Column(String(45))


class Side(Base):
    __tablename__ = 'sides'

    id_side = Column(Integer, primary_key=True)
    name_side = Column(String(45))


class Doctor(Base):
    __tablename__ = 'doctors'
    __table_args__ = {'comment': 'List of operating doctors '}

    id_doctor = Column(Integer, primary_key=True)
    title = Column(String(45))
    first_name = Column(String(45))
    last_name = Column(String(45))
    id_department = Column(ForeignKey('departments.id_department'), index=True)
    username = Column(String(45))
    password = Column(String(128))

    department = relationship('Department')


class Patient(Base):
    __tablename__ = 'patients'
    __table_args__ = {'comment': 'Data characterizing the patient '}

    id_patient = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    date_birth = Column(Date)
    gender = Column(String(45))
    id_insurance = Column(ForeignKey('insurances.id_insurance'), index=True)

    insurance = relationship('Insurance')


class SurgeryProcedure(Base):
    __tablename__ = 'surgery_procedures'

    snomed_code = Column(Integer, primary_key=True)
    name = Column(String(45))
    typical_dpt_id = Column(ForeignKey('departments.id_department'), index=True)

    typical_dpt = relationship('Department')


class OperationsTakenPlace(Base):
    __tablename__ = 'operations_taken_place'

    id_operation = Column(Integer, primary_key=True)
    id_patient = Column(ForeignKey('patients.id_patient'), index=True)
    snomed_code = Column(ForeignKey('surgery_procedures.snomed_code'), index=True)
    id_side = Column(ForeignKey('sides.id_side'), index=True)
    id_doctor = Column(ForeignKey('doctors.id_doctor'), index=True)
    date = Column(Date)
    check_list = Column(Integer)
    id_outcome = Column(ForeignKey('postop_procedure.id_outcome'), index=True)
    comments = Column(LONGTEXT)
    pictures = Column(LONGBLOB)

    doctor = relationship('Doctor')
    postop_procedure = relationship('PostopProcedure')
    patient = relationship('Patient')
    side = relationship('Side')
    surgery_procedure = relationship('SurgeryProcedure')
