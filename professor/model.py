from .dbProfessor import Professor
from config import db

class ProfessorNaoEncontrado(Exception):
    pass

def getListProfessor():
    professores = Professor.query.all()
    return [professor.to_dict() for professor in professores]

def getProfessorById(idProfessor):
    professor = Professor.query.get(idProfessor)
    if not professor:
        raise ProfessorNaoEncontrado
    return professor.to_dict()

def addProfessor(dict):
    novoProfessor = Professor(nome = dict['nome'], idade = dict['idade'], materia = dict['materia'], observacoes = dict['observacoes'])
    db.session.add(novoProfessor)
    db.session.commit()

def updateProfessorById(idProfessor, dict):
    professor = Professor.query.get(idProfessor)
    if not professor:
        raise ProfessorNaoEncontrado
    
    if dict.get('nome') is not None:
        professor.nome = dict['nome'] 
    if dict.get('idade') is not None:
        professor.idade = dict['idade']
    if dict.get('materia') is not None:
        professor.materia = dict['materia']
    if dict.get('observacoes') is not None:
        professor.observacoes = dict['observacoes']
   
    db.session.commit()
    

def deleteProfessorById(idProfessor):
    professor = Professor.query.get(idProfessor)
    if not professor:
        raise ProfessorNaoEncontrado
    db.session.delete(professor)
    db.session.commit()
  