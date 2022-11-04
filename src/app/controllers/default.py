from app import app,db
from flask import render_template, redirect, url_for
from flask.globals import request
from app.models.model import Chamado, User
import datetime


# aqui atribuimos uma routa para essa aplicação com .route ligado a nossa aplicação flask e atribuimos um caminho como "/" que quer dizer a raiz do site e ela vai sempre executar a função que estiver em seguida dela como é caso ela executa a função home page
@app.route("/")
def homepage():
    # na função home page você utiliza uma função da biblioteca padrão do flask a render_template() para você renderizar uma pagina html e não ter que poluir seu condigo com tags de html e todos os arquivos htmls devem ficar em uma pasta chamada templates com essa escrita e ficando no mesmo diretorio do arquivo.py que está sua aplicação flask
    return render_template("home.html")


<<<<<<< Updated upstream


@app.route("/abertura")
def abertura_de_chamado():
    return render_template("abertura-de-chamado.html")




# função e rota para visualizar os chamados 
@app.route("/visualizar")
=======
@app.route("/index")
@app.route("/")
def homepage():
    """Função e rota da página home"""
    return render_template("home.html")



@app.route("/obrigado")
def obrigado():
    return render_template("obrigado.html")



# função e rota para visualizar os chamados
@app.route("/visualizar", methods=["POST", "GET"])
>>>>>>> Stashed changes
def visualizar():
    #depois você utiliza return com a fundação render_template("atribuindo a rota que você quer", além de adicionar a uma variavel tabela o valor da tabela que é lista do banco para que você possa utilizar os valores dela no seu html quando renderizar ele)
    tabela = Chamado.query.order_by(Chamado.id).all()
    return render_template("visualizar.html", tabela=tabela)




# função e rota para cadastrar que recebe do html o dados do formulario e cria uma variavel chamado com o modelo Chamado(atribuindo os valores do formulario para cada campo) e depois redireciona você para raiz
@app.route("/cadastrar", methods=["POST", "GET"])
def cadastrar():
    lab = int(request.form["lab"])
    comp = int(request.form["comp"])
    problem = request.form["problem_type"]
    description = request.form["description"]
    time_created = datetime.datetime.now()
    chamado = Chamado(lab, comp, problem, description, 'Pendente', time_created, 1)
    db.session.add(chamado)
    db.session.commit()
    return redirect("/")



# rota que deleta o chamdo do id que você colocar no caminho por ex:/deletar/2 vai deletar o chamado de id 2
@app.route('/deletar/<int:id>')
def deletar(id):
    r = Chamado.query.filter_by(id=id).first()
    db.session.delete(r)
    db.session.commit()
    return redirect("/visualizar")


# função de atualizar o chamado do id informado que vai entrar em uma pagina para a pessoa preencher as modificações e assim vai pegar as informações e atualizar no banco de dados
@app.route('/atualizar/<int:id>', methods=["POST", "GET"])    
def atualizar(id):
    r = Chamado.query.filter_by(id=id).first()
    
    if request.method == "POST":
        
        r.lab = request.form["lab"]
        r.comp = request.form["comp"]
        r.description = request.form["description"]
        db.session.add(r)
        db.session.commit()
        #flash("Atualizado")
        return redirect(url_for('visualizar'))
    return render_template("atualizar.html", r=r)




<<<<<<< Updated upstream
=======
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
@app.route("/lab", methods=["POST", "GET"])
def lab():
    return render_template('Portas.html')




# Rota de dos problemas
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
                
            total = request.form['totalcontent']
            
                
            msg = "Sala criada com sucesso"

               

         elif (request.form['actiontype'] == "del"):
            nome = request.form['salalist']
            lay= Object.query.filter_by(Object_lab=nome).all()
            for item in lay:
                dell(Object, item.id)
            msg = "Deletada com sucesso"
            

         elif (request.form['actiontype'] == "save"):
            nome = request.form['salalist']
            total = request.form['totalcontent']
            elements=request.form['elementcontent']   
            elements = elements.split('\n')
            lay = Object.query.filter_by(Object_lab=nome).all()
            for item in elements:
                index = item.find('id="')
                for item2 in lay:
                    if item[index:index+15] in item2.Object_div:
                        print('está dentro')
                
            
            
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
>>>>>>> Stashed changes
