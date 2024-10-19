import os
from .dbTurma import Turma
from config import db
from professor.model import *

class TurmaNaoEncontrada(Exception):
    pass

def getListTurma():
    getListProfessor()
    turma = Turma.query.all()
    return [turma.to_dict() for turma in turma]

def getTurmaById(idturma):
    turma = Turma.query.get(idturma)
    if not turma:
        raise TurmaNaoEncontrada
    return turma.to_dict()
    
def addTurma(dict):
    professor = getProfessorById(dict['professor'])
    if not professor:
        raise ProfessorNaoEncontrado

    novaTurma= Turma(
        id=dict['id'],
        descricao=dict['descricao'], 
        professor=dict['professor'],
        ativo=dict['ativo'])
    db.session.add(novaTurma)
    db.session.commit()

def atualizacaoTurmaById(idTurma,dict):     
    turma = Turma.query.get(idTurma)
    if not turma:
        raise TurmaNaoEncontrada
    if dict.get('descricao') is not None:
        turma.nome = dict['descricao'] 
    if dict.get('professor') is not None:
        professor = getProfessorById(dict['professor'])
        if not professor:
            raise ProfessorNaoEncontrado
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
    



