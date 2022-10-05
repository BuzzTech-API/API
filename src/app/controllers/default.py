from app import app, db
from flask import render_template, redirect, url_for, request
from app.models.model import Chamado, User
from flask_login import login_user, logout_user
import datetime


# aqui atribuimos uma routa para essa aplicação com .route ligado a nossa aplicação flask e atribuimos um caminho como "/" que quer dizer a raiz do site e ela vai sempre executar a função que estiver em seguida dela como é caso ela executa a função home page
@app.route("/index")
@app.route("/")
def homepage():
    # na função home page você utiliza uma função da biblioteca padrão do flask a render_template() para você renderizar uma pagina html e não ter que poluir seu condigo com tags de html e todos os arquivos htmls devem ficar em uma pasta chamada templates com essa escrita e ficando no mesmo diretorio do arquivo.py que está sua aplicação flask
    return render_template("home.html")



@app.route("/abertura")
def abertura_de_chamado():
    return render_template("abertura-de-chamado.html")



# função e rota para visualizar os chamados 
@app.route("/visualizar")
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



@app.route('/cadastrar_login', methods=['GET','POST'])
def cadastrar_login():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('cadastrar.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.verify_password(password):
            print(user.verify_password(password))
            login_user(user)
            return redirect(url_for('visualizar'))
        
        
        print("Usuário não existe")
        return redirect(url_for('homepage'))

    return render_template('login.html')



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))
