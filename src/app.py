from flask import Flask, render_template, redirect
from connect import Update_Call, Search_Call, Del_Call, insert, Show_All
from flask.globals import request
from model import Chamado

# o app atribuimos a ele nossa aplicação flask
app = Flask(__name__)

# aqui atribuimos uma routa para essa aplicação com .route ligado a nossa aplicação flask e atribuimos um caminho como "/" que quer dizer a raiz do site e ela vai sempre executar a função que estiver em seguida dela como é caso ela executa a função home page
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
    #primeiro você atribui a variavel tabela a lista do banco de dados com a função criada no connect.py
    tabela= Show_All()
    #depois você utiliza return com a fundação render_template("atribuindo a rota que você quer", além de adicionar a uma variavel tabela o valor da tabela que é lista do banco para que você possa utilizar os valores dela no seu html quando renderizar ele)
    return render_template("visualizar.html", tabela=tabela)




# função e rota para cadastrar que recebe do html o dados do formulario e cria uma variavel chamado com o modelo Chamado(atribuindo os valores do formulario para cada campo) e depois redireciona você para raiz
@app.route("/cadastrar", methods=["POST", "GET"],)
def cadastrar():
    lab = request.form["lab"]
    comp = request.form["comp"]
    problem_type = request.form["problem_type"]
    description = request.form["description"]
    chamado = Chamado(0,lab, comp,problem_type, description)
    insert(chamado)
    return redirect("/")



# rota que deleta o chamdo do id que você colocar no caminho por ex:/deletar/2 vai deletar o chamado de id 2
@app.route('/deletar/<int:id>')
def deletar(id):
    # assim que entra na função ele tentar deletar o chamado com a função feita connect.py e redireciona você para pagina de visualização
    try:
        Del_Call(id)
        return redirect("/visualizar")
    
    # caso ocorra um porblema ele entra no except redireciona você para pagina de visualização
    except:
        return redirect("/visualizar")



# função de atualizar o chamado do id informado que vai entrar em uma pagina para a pessoa preencher as modificações e assim vai pegar as informações e atualizar no banco de dados
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


