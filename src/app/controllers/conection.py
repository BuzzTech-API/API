from app import db
from app.models.model import Chamado, User, Object
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
    return




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

def pao(elements, lay, nome):
    for i in range(len(elements)):
                index = elements[i].find('obj')
                if index!=-1:
                    cont=0
                    for item2 in lay:
                        
                        if elements[i][index:index+8] in item2.Object_div:
                            if 'class="pc"' in elements[i]:
                                index=elements[i].find('innertext')
                                index2=elements[i].find('</div>')
                                item2.Object_compname = elements[i][index+11:index2]
                                item2.Object_div=elements[i]
                                db.session.add(item2)
                                db.session.commit()
                                cont=0
                                break
                            else:
                                item2.Object_div=elements[i]
                                db.session.add(item2)
                                db.session.commit()
                                cont=0
                                break
                        cont+=1 
                    if cont!=0:
                        if 'class="pc"' in elements[i]:
                            index=elements[i].find('innertext')
                            index2=elements[i].find('</div>')
                            params={
                                'Object_lab': nome,
                                'Object_div': elements[i]+'\n',
                                'Object_compname':elements[i][index+11:index2],
                                'Object_comp_processor':"",
                                'Object_comp_RAM': '',
                                'Object_comp_operational_system':''
                            }
                            insert(Object, params)
                        elif 'class="':
                            params={
                                'Object_lab': nome,
                                'Object_div': elements[i] + '\n',
                                'Object_compname':'',
                                'Object_comp_processor':"",
                                'Object_comp_RAM': '',
                                'Object_comp_operational_system':''
                            }
                            insert(Object, params)