from app import app, db
from flask import render_template, redirect, url_for, request
from app.models.model import Chamado, User, Object
from flask_login import logout_user
import datetime
# Funções de interação com o banco de dados está fora do arquivo para melhor a legibilidade do código
from app.controllers.conection import dell, update_call, user_login, insert, pao






@app.route("/index")
@app.route("/")
def homepage():
    """Função e rota da página home"""
    return render_template("home.html")



@app.route("obrigado")
def obrigado():
    return render_template("obrigado.html")

    

# função e rota para visualizar os chamados
@app.route("/visualizar", methods=["POST", "GET"])
def visualizar():
    """Função e rota de visualização dos chamados"""
    tabela = Chamado.query.order_by(Chamado.id).all()
    element=[]
    element1=[]
    for item in tabela:
        obj=Object.query.filter_by(id=item.Object_id).first()
        element.append(obj.Object_lab)
        element1.append(obj.Object_compname)

    return render_template("visualizar.html", tabela=tabela, comp=element1, lab=element, len=len(element))



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
    l = Object.query.filter_by(id=r.Object_id).first()
    if request.method == "POST":
        update_call(r)
        # flash("Atualizado")
        return redirect(url_for('visualizar'))
    return render_template("atualizar.html", chamado=r, comp=l)



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
@app.route('/<lab>/', methods=["POST", "GET"])
def comp(lab):
    l = Object.query.filter_by(Object_lab=lab)
    return render_template('Lab.html',lab=lab, elmnts=l)




# Rota de laboratorio
@app.route('/lab', methods=["POST", "GET"])
def lab():
    return render_template('Portas.html')




# Rota de seleção dos problemas
@app.route('/<lab>/<comp>/seleção_problemas', methods=["POST", "GET"])
def seleção_problemas(lab, comp):
    """Rota de selecionar os chamados e finalizar o cadastro do chamado"""
    l = Object.query.filter_by(id=comp).first()
    if request.method == "POST": 
        params={
        "Object_id":comp,
        "Problem": request.form["problem"],
        "Description": request.form["description"],
        "Status": 'Pendente',
        "Time_created":datetime.datetime.now(),
        "User_id":1
        }
        insert(Chamado, params)   
        return redirect(url_for('obrigado'))

    return render_template('Seleção de Problemas.html',lab=lab,comp=l)


@app.route('/editar', methods = ['POST', 'GET'])
def editar():
    l = Object.query.order_by(Object.Object_lab)
    labs=[]
    for item in l:
        if item.Object_lab not in labs:
            labs.append(item.Object_lab)

    return render_template('edit.html', labs=labs)

@app.route('/edited', methods = ['POST', 'GET'])
def edited():
   elmnts = ""
   if request.method == 'POST':
      try:
         selected = request.form["selectedvalue"]

         if (request.form['actiontype'] == "add"):
            nome = request.form['txtnew']
            elements = request.form['elementcontent']
            elements = elements.split('\n')
            for item in elements:
                if 'class="pc"' in item:
                    index=item.find('innertext')
                    index2=item.find('</div>')
                    params={
                        'Object_lab': nome,
                        'Object_div': item+'\n',
                        'Object_compname':item[index+11:index2],
                        'Object_comp_processor':"",
                        'Object_comp_RAM': '',
                        'Object_comp_operational_system':''

                    }
                    insert(Object, params)
                elif 'class="':
                    params={
                        'Object_lab': nome,
                        'Object_div': item + '\n',
                        'Object_compname':'',
                        'Object_comp_processor':"",
                        'Object_comp_RAM': '',
                        'Object_comp_operational_system':''
                    }
                    insert(Object, params)
                
            
                
            msg = "Sala criada com sucesso"

               

         elif (request.form['actiontype'] == "del"):
            nome = request.form['salalist']
            lay= Object.query.filter_by(Object_lab=nome).all()
            for item in lay:
                dell(Object, item.id)
            msg = "Deletada com sucesso"
            

         elif (request.form['actiontype'] == "save"):
            nome = request.form['salalist']
            elements=request.form['elementcontent']   
            elements = elements.split('\n')
            lay = Object.query.filter_by(Object_lab=nome).all()
            print(len(lay))
            pao(elements,lay, nome)
            lay = Object.query.filter_by(Object_lab=nome).all()

                        
                
            
            
            msg = "Sala modificada com sucesso"
            

         elif (request.form['actiontype'] == "load"):
            
            
            nome = request.form['salalist']
            lay=Object.query.filter_by(Object_lab=nome).all()
            elmnts = []
            for item in lay:
                elmnts.append(item.Object_div)

            
            msg = "Sala carregada com sucesso"

      except:
         msg = ("ERRO")

      finally:
        lay=Object.query.order_by(Object.Object_lab)
        labs=[]
        for item in lay:
            if item.Object_lab not in labs:
                labs.append(item.Object_lab)
        return render_template("edit.html", labs = labs, selected = selected, msg = msg, elmnts = elmnts)