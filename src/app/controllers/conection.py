from app import db
from app.models.model import Chamado, User, Object
from flask import render_template, redirect, url_for, request
from flask_login import login_user
from datetime import datetime
import mysql.connector

conexao = mysql.connector.connect(
    host='35.174.216.24',
    user='fatec',
    password='fatec',
    database='api',
    port=3306,
    )
cursor= conexao.cursor()

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
    chamado.Problem = request.form["problem"]
    chamado.Description = request.form["description"]
    chamado.Status = request.form["status"]
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

def update_object(elements, lay, nome):
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

def delete_object(elements, lay):
    for item in lay:
        # procurando em cada tupla
        Object_div = item.Object_div
        c = 0
        for item2 in elements:
            # para cada tupla, procurar objeto por objeto
            index = item2.find('obj')
            if index == -1:
                # se o objeto tá vazio
                c = c
            elif item2[index:index+8] in Object_div:
                # se o objeto tá na tupla
                c += 1
                break
            else :
                c = c
        if c == 0:
            dell(Object, item.id)


def mostrar_chamado_aberto(lab):
    conexao.reconnect()
    comando=f'SELECT * from object WHERE Object_lab={lab}'
    cursor= conexao.cursor()
    cursor.execute(comando)
    l = cursor.fetchall()
    lista=[]
    for item in l:
        lista.append([item[0],item[1],item[2],item[3]])
    comando=f'SELECT Object_id from calls'
    cursor= conexao.cursor()
    cursor.execute(comando)
    tabela= cursor.fetchall()
    print(tabela)
    cursor.close()
    for item in tabela:
        comando=f'SELECT * FROM object WHERE id={item[0]}'
        cursor= conexao.cursor()
        cursor.execute(comando)
        item2=cursor.fetchone()
        index1=item2[2].find('style="')+7
        item3=item2[2]
        item3=item3[:index1]+'background-color: rgba(255, 0, 0, 0.3); border-radius: 10px; filter: drop-shadow(2px 4px 6px red); '+item3[index1:]
        for item in lista:
            if item[0]==item2[0]:
                item[2]=item3
        cursor.close()
    return lista
