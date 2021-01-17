#Here we declare all the tables - try to take the target names of the database!

# import things
from flask_table import Table, Col

# Declare your table
class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')


class ResultsDoc(Table):
    id_operation = Col('Id', show=True)
    id_patient = Col("Patient")
    snomed_code = Col("Snomed Code")
    id_doctor = Col("Surgeon")
    


    #date = Col('Release Date')
    #patient_id = Col('Patient ID')
    #patient_last_name = Col('Last Name')
    #patient_first_name = Col('First Name')
    #patient_gender = Col('Sex')
    #date_birth = Col('Date of birth')
    #surgery_procedure_name = Col('Operation')


class ResultsDocItems(object):
    def __init__(self, name, description):
        self.id_operation = name
        self.id_patient = id_patient
        self.snomed_code = snomed_code
        self.id_doctor = id_doctor
        
        #self.date = date
        #self.patient_id = patient_id
        #self.patient_last_name = patient_last_name
        #self.patient_first_name = patient_first_name
        #self.patient_gender = patient_gender
        #self.date_birth = date_birth
        #self.surgery_procedure_name = surgery_procedure_name




   
class ResultsDep(Table):
    id_operation = Col('Id', show=True)
    department_name = Col('Department')
    date = Col('Release Date')
    patient_id = Col('Patient ID')
    patient_last_name = Col('Last Name')
    patient_first_name = Col('First Name')
    patient_gender = Col('Sex')
    date_birth = Col('Date of birth')
    surgery_procedure_name = Col('Operation')


class ResultsDepItems(object):
    def __init__(self, name, description):
        self.id_operation = name
        self.department_name = department_name
        self.date = date
        self.patient_id = patient_id
        self.patient_last_name = patient_last_name
        self.patient_first_name = patient_first_name
        self.patient_gender = patient_gender
        self.date_birth = date_birth
        self.surgery_procedure_name = surgery_procedure_name
        