####CONFIG FILE####
# CAREFUL HERE #


from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))



class Config:
    """Base config."""
   
    SECRET_KEY = 'vanessa'
    SESSION_COOKIE_NAME = "SAFENSURG"
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    FLASK_APP = 'runserver.py'

    #### Database config. ####

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI =  "mysql://root:vanessa@127.0.0.1/surgeries_db"
    SQLALCHEMY_ECHO = True

    ####UPLOAD CONFIG ###
    UPLOADED_IMAGES_DEST = "uploads/images"



#class ProdConfig(Config):
   # FLASK_ENV = 'production'
    #DEBUG = False
    #TESTING = False
    #DATABASE_URI = environ.get('PROD_DATABASE_URI')


#class DevConfig(Config):
    #FLASK_ENV = 'development'
    #DEBUG = True
    #TESTING = True
    #DATABASE_URI = environ.get('DEV_DATABASE_URI')