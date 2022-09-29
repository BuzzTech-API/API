from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

#A estrutura de informações que tem em um chamado

class Chamado(db.Model):
    
    __tablename__ = "calls"
    id = db.Column(db.Integer, primary_key=True)
    lab = db.Column(db.Integer, nullable=False)
    comp = db.Column(db.Integer, nullable=False)
    problem = db.Column(db.String(200),nullable=False)
    description = db.Column(db.String(400),nullable=False)
    status = db.Column(db.String(200),nullable=False)
    
    
    def __init__(self,lab, comp, problem, description, status) -> None:
        self.lab = lab
        self.comp = comp
        self.problem = problem
        self.description = description
        self.status = status

