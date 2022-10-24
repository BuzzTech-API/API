import time
from app import app, db
from flask import render_template, redirect, url_for, request
from app.models.model import Chamado, User
from flask_login import logout_user
import datetime
# Funções de interação com o banco de dados está fora do arquivo para melhor a legibilidade do código
from app.controllers.conection import dell, update_call, user_login, insert






@app.route("/index")
@app.route("/")
def homepage():
    """Função e rota da página home"""
    return render_template("home.html")



# função e rota para visualizar os chamados
@app.route("/visualizar", methods=["POST", "GET"])
def visualizar():
    """Função e rota de visualização dos chamados"""
    tabela = Chamado.query.order_by(Chamado.id).all()
    return render_template("visualizar.html", tabela=tabela)



# rota que deleta o chamdo do id que você colocar no caminho por ex:/deletar/2 vai deletar o chamado de id 2
@app.route('/deletar/<int:id>')
def deletar(id):
    """Função que deleta chamado"""
    dell(Chamado,id)
    return redirect("/visualizar")



# função de atualizar o chamado do id informado que vai entrar em uma pagina para a pessoa preencher as modificações e assim vai pegar as informações e atualizar no banco de dados
@app.route('/atualizar/<int:id>', methods=["POST", "GET"])
def atualizar(id):
    r = Chamado.query.filter_by(id=id).first()
    if request.method == "POST":
        update_call(r)
        # flash("Atualizado")
        return redirect(url_for('visualizar'))
    return render_template("atualizar.html", chamado=r)



@app.route('/cadastrar_login', methods=['GET', 'POST'])
def cadastrar_login():
    if request.method == 'POST':
        params={
        'name': request.form['name'],
        'email': request.form['email'],
        'password': request.form['password']
        }
        insert(User, params)
        return redirect(url_for('login'))
    return render_template('cadastrar.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_login(request.form['email'], request.form['password'])
        return redirect(url_for('homepage'))
    return render_template('login.html')



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))



# Rota de portas
@app.route('/<int:lab>/', methods=["POST", "GET"])
def comp(lab):
    return render_template('Lab.html',lab=lab)




# Rota de laboratorio
@app.route('/lab', methods=["POST", "GET"])
def lab():
    return render_template('Portas.html')




# Rota de dos problemas
@app.route('/<int:lab>/<int:comp>/seleção_problemas', methods=["POST", "GET"])
def seleção_problemas(lab, comp):
    """Rota de selecionar os chamados e finalizar o cadastro do chamado"""
    if request.method == "POST": 
        params={
        "lab":lab,
        "comp":comp,
        "problem": request.form["problem"],
        "description": request.form["description"],
        "status": 'Pendente',
        "time_created":datetime.datetime.now(),
        "user_id":1
        }
        insert(Chamado, params)   
        return redirect(url_for('homepage'))

    return render_template('Seleção de Problemas.html',lab=lab,comp=comp)





