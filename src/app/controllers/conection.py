from app import db
from app.models.model import Chamado, User
from flask import render_template, redirect, url_for, request
from flask_login import login_user




# Função de inserção de chamado no banco
def Insert_call(lab, comp, problem, description,time_created, status, user_id):
    chamado = Chamado(lab, comp, problem, description,time_created, status, user_id)
    db.session.add(chamado)
    db.session.commit()
    return print('inserido')




# Função de deletar de chamado no banco
def Dell_call(id):
    r = Chamado.query.filter_by(id=id).first()
    db.session.delete(r)
    db.session.commit()
    return redirect("/visualizar")




# Função de atualizar de chamado no banco
def Update_call(chamado):
    chamado.lab = request.form["lab"]
    chamado.comp = request.form["comp"]
    chamado.description = request.form["description"]
    db.session.add(chamado)
    db.session.commit()
    return 'Atualizado'




# Função de logar usuario
def User_login(email, password):
    user = User.query.filter_by(email=email).first()

    if user and user.verify_password(password):
        print(user.verify_password(password))
        login_user(user)
        return redirect(url_for('visualizar'))
    return "Usuário não existe"





# Função de cadastrar login
def Insert_login(name,email,password):
    user = User(name=name, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return 'Inserido usuário'