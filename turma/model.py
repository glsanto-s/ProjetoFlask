from dbTurma import Turma
from config import db 

class TurmaNaoEncontrada(Exception):
    pass

def getListTurma():
    turma = Turma.query.all()
    return [turma.to_dict() for turma in turma]

def getTurmaById(idturma):
    turma = Turma.query.get(idturma)
    if not turma:
        raise TurmaNaoEncontrada
    return turma.to_dict()
    
def addTurma(dict):
    novaTurma= Turma(id=dict['id'],descricao=dict['descricao'], professor=dict['professor'],ativo=dict['ativo'])
    db.session.add(novaTurma)
    db.session.commit()

def atualizacaoTurmaById(idTurma,dict):     
    turma = Turma.query.get(idTurma)
    if not turma:
        raise TurmaNaoEncontrada
    if dict.get('descricao') is not None:
        turma.nome = dict['descricao'] 
    if dict.get('professor') is not None:
        turma.nome = dict['professor'] 
    if dict.get('ativo') is not None:
        turma.nome = dict['ativo'] 
    db.session.commit ()

    
def excluirTurmaById(idturma):
    turma = Turma.query.get(idturma)
    if not turma:
        raise TurmaNaoEncontrada
    db.session.delete(turma)
    db.session.comit()
    



