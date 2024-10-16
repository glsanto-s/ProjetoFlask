from dbProfessor import Professor
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

def validaProfessorExist(idProfessor):
    try:
        getProfessorById(idProfessor)
        return True
    except Exception:
        return False

def addProfessor(dict):
    novoProfessor = Professor(nome = dict['nome'], idade = dict['idade'], materia = dict['materia'], observacoes = dict['observacoes'])
    db.session.add(novoProfessor)
    db.session.commit()

def updateProfessorById(idProfessor, dict):
    validacao = validaProfessorExist(idProfessor)
    if validacao is True:
        professor = Professor(nome = dict['nome'], idade = dict['idade'], materia = dict['materia'], observacoes = dict['observacoes'])
        db.session.commit()
    else:
        raise ProfessorNaoEncontrado

def deleteProfessorById(idProfessor):
    professor = getProfessorById(idProfessor)
    if not professor:
        raise ProfessorNaoEncontrado
    db.session.delete(aluno)
    db.session.commit()
  