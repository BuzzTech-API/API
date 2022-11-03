
DEBUG = True

# Para utilização do banco local. Trocar para:
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:'senhalocal'@localhost:3306/api'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://fatec:fatec@35.174.216.24:3306/api'

SECRET_KEY = "SECRET"
SQLALCHEMY_TRACK_MODIFICATIONS = True
