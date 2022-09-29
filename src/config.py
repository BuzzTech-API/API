import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/api' 
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bf0d1c3912678e:87be5aa2@us-cdbr-east-06.cleardb.net/heroku_c8f77d4e882bc27'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'secret'