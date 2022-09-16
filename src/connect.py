from model import Chamado
from tinydb import *
import pandas as pd

bd = TinyDB("Chamados.json")
chamado = Query()

def insert(model: Chamado):
    model.id = len(bd)
    if len(bd)==0:
        model.id = 1
        bd.insert({"id":model.id, "lab":model.lab, "comp":model.comp, "problem_type":model.problem_type,"description":model.description})
    else:
        model.id=len(bd)+1
        bd.insert({"id":model.id, "lab":model.lab, "comp":model.comp, "problem_type":model.problem_type,"description":model.description})

def insert_update(model: Chamado):
    bd.insert({"id":model.id, "lab":model.lab, "comp":model.comp, "problem_type":model.problem_type,"description":model.description})


def decrement(id:int):
    id=id-1
    return id 

def Show_All():
    todos = bd.all()
    return todos


def Del_Call(id: int):
    if bd.search(chamado.id==id):
        temporaria=len(bd)
        bd.remove(chamado.id==id)
        tabela=Show_All()
        for item in tabela:
            print(item)
            if item['id']>id: 
                novoID=item['id']-1
                bd.update({'id': novoID}, chamado.id==item['id'])
        print("Chamado apagado com sucesso")
    else:
        print("id não encontrado")
        
                


def Update_Call(id: int, model: Chamado):
    if bd.search(chamado.id==id):
        model.id = id
        bd.update({'id': id, 'lab': model.lab, 'comp': model.comp, 'problem_type': model.problem_type, 'description': model.description }, chamado.id==id)

        #insert_update(model)
    else:
        print("Esse chamado não existe")


def mostrarTabelaTodos():
    todos = pd.DataFrame(bd)
    return todos

def Search_Call(id: int):
    return bd.search(chamado.id==id)



#CRUD = Create/Read/Update/Delete
