from model import Chamado
from tinydb import *

# bd é variavél que se refere ao banco de dados sempre que ver bd.algo é uma função da biblioteca tinyDB interagindo com o banco
bd = TinyDB("Chamados.json")
# chamado é a query uma função do tinyDB para realizar busca dentro do banco de dados e saber se uma informação 
chamado = Query()

#Função que adiciona uma chamado no banco de dados
def insert(model: Chamado):
    #primeiramente ela verifica o tamanho da lista do banco de dados para poder dar o valor para o id
    model.id = len(bd)
    if len(bd)==0: #aqui ela compara se o tamanho do banco é 0, ou seja, não existe chamado cadastrado
        model.id = 1
        #assim ela atribui para o valor de id como 1 e insere no banco de dados as informações que foram recebidas pelo usuario
        bd.insert({"id":model.id, "lab":model.lab, "comp":model.comp, "problem_type":model.problem_type,"description":model.description})
    else:
        # Caso seja diferente de 0 ele vai pegar o tamanho da lista e vai adicionar pq o proximo chamado vai ser o novo tamanho da lista
        model.id=len(bd)+1
        # e faz a inserção das informações de novo
        bd.insert({"id":model.id, "lab":model.lab, "comp":model.comp, "problem_type":model.problem_type,"description":model.description})




# é função que mostra tudo que está no banco de dados em formato de lista
def Show_All():
    todos = bd.all()
    return todos


# Função que apaga um chamado do banco
def Del_Call(id: int):
    # primeiro a função pesquisa se o chamado existe no banco se ele existir ela entra no if
    if bd.search(chamado.id==id):
        # dentro do if ela remove o chamado do banco
        bd.remove(chamado.id==id)
        # você depois atribui a tabela a função de mostrar tudo que está no banco em lista
        tabela1=Show_All()
        # Você faz um for para o tamanho da lista em tabela você vai atribuir a item essa posição da lista
        for item in tabela1:
            # Agora você faz uma comparação se o id do que você removeu é menor que o que você está na lista agora, se sim você reduz o valor dele em 1 para que sempre os id fique enumerados de forma crescente e nunca fique com um vacuo por ex: 1, 3, 5, assim evitando o problema na hora de adicionar novos chamados
            if item['id']>id: 
                novoID=item['id']-1
                bd.update({'id': novoID}, chamado.id==item['id'])
        print("Chamado apagado com sucesso")
    
    # se não ela so diz no terminal que ele não existe
    else:
        print("id não encontrado")
        
                


# Função que atualiza o chamado ela recebe já o modelo de chamado com as informações para atualizar
def Update_Call(id: int, model: Chamado):
    # primeiro a função pesquisa se o chamado existe no banco se ele existir ela entra no if
    if bd.search(chamado.id==id):
        # ela atribui ao valor do modelo o id do chamado que está sendo editado e atualiza ele no banco
        model.id = id
        bd.update({'id': id, 'lab': model.lab, 'comp': model.comp, 'problem_type': model.problem_type, 'description': model.description }, chamado.id==id)

# se não ela so diz no terminal que ele não existe
    else:
        print("Esse chamado não existe")


# função que procura se existe um chamado no banco de dados e o retorna
def Search_Call(id: int):
    return bd.search(chamado.id==id)



