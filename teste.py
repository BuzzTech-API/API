from crypt import methods
from flask import Flask, render_template, redirect
from connect import Update_Call, Search_Call, Del_Call, insert, mostrarTabelaTodos, Show_All
from flask.globals import request
from model import Chamado

app = Flask(__name__)
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/visualizar")
def visualizar():
    tabela= Show_All()
    
    return render_template("visualizar.html", tabela=tabela)

@app.route("/cadastrar", methods=["POST", "GET"],)
def cadastrar():
    lab = request.form["lab"]
    comp = request.form["comp"]
    problem_type = request.form["problem_type"]
    description = request.form["description"]
    chamado = Chamado(0,lab, comp,problem_type, description)
    insert(chamado)
    return redirect("/")

@app.route('/deletar/<int:id>')
def deletar(id):
    try:
        Del_Call(id)
        return redirect("/visualizar")
    except:
        return redirect("/visualizar")

@app.route('/atualizar/<int:id>', methods=["POST", "GET"])    
def atualizar(id):
    if request.method=='POST':
        lab = request.form["lab"]
        comp = request.form["comp"]
        problem_type = request.form["problem_type"]
        description = request.form["description"]
        chamado = Chamado(id,lab, comp,problem_type, description)
        try:
            Update_Call(id, chamado)
            return redirect('/visualizar')
        except:
            return 'Algo deu errado', redirect('/visualizar')
    
    else:
        chamado = Search_Call(id)
        return render_template('atualizar.html', chamado= chamado, id = id)




if __name__ == "__main__":
    app.run(debug=True) 

