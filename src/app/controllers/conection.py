from app import db
from app.models.model import Chamado, User
from flask import render_template, redirect, url_for, request
from flask_login import login_user
from datetime import datetime


# Função de inserção de tupla no banco
def insert(Model, params):
    """Função para inserir em uma tabela uma tupla no banco de dados"""
    if Model == User:
        model= Model(name=params.get('name'), email=params.get('email'), password=params.get('password'))
    else:
        model = Model(params)
    db.session.add(model)
    db.session.commit()
    return


# Função de deletar de tupla no banco
def dell(Model,id):
    '''Função de deletar de tupla no banco'''
    r = Model.query.filter_by(id=id).first()
    db.session.delete(r)
    db.session.commit()
    return redirect("/visualizar")




# Função de atualizar de chamado no banco
def update_call(chamado):
    '''Função de atualizar os chamado no banco'''
    chamado.lab = request.form["lab"]
    chamado.comp = request.form["comp"]
    chamado.problem = request.form["problem"]
    chamado.description = request.form["description"]
    db.session.add(chamado)
    db.session.commit()
    return 'Atualizado'




# Função de logar usuario
def user_login(email, password):
    '''Função de logar usuario'''
    user = User.query.filter_by(email=email).first()

    if user and user.verify_password(password):
        print(user.verify_password(password))
        login_user(user)
        return redirect(url_for('visualizar'))
    return "Usuário não existe"
