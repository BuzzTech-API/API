from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


#A estrutura de informações que tem em um chamado


class Chamado(db.Model):
    
    __tablename__ = "calls"
    id = db.Column(db.Integer, primary_key=True)
    lab = db.Column(db.Integer, nullable=False)
    comp = db.Column(db.Integer, nullable=False)
    problem = db.Column(db.String(60),nullable=False)
    description = db.Column(db.String(400),nullable=False)
    status = db.Column(db.String(60),nullable=False)
    time_created = db.Column(db.Date,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    """def __init__(self,lab, comp, problem, description, status, time_created,user_id):
        self.lab = lab
        self.comp = comp
        self.problem = problem
        self.description = description
        self.status = status
        self.time_created = time_created
        self.user_id = user_id"""
    def __init__(self, params):
        self.lab = params.get('lab')
        self.comp = params.get('comp')
        self.problem = params.get('problem')
        self.description = params.get('description')
        self.status = params.get('status')
        self.time_created = params.get('time_created')
        self.user_id = params.get('user_id')



#Login Stuff
@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(120),nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    chamados = db.relationship('Chamado', backref='users')


    @property
    def password(self):
        raise AttributeError ('password is not a readable attribute!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
