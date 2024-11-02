from .dbAluno import Aluno
from config import db
from turma.model import *

class AlunoNaoEncontrado(Exception):
    pass

def getAlunoByid(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    return aluno.to_dict()

def getlistarAlunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]

def adicionar_aluno(dict):
    turma = getTurmaById(dict['turma'])
    if not turma:
        raise TurmaNaoEncontrada
    novoAluno = Aluno(
        nome = dict['nome'], 
        idade = dict['idade'], 
        turma = dict['turma'], 
        data_nascimento = dict['data_nascimento'], 
        nota_primeiroSemestre = dict['nota_primeiroSemestre'], 
        nota_segundoSemestre = dict['nota_segundoSemestre'], 
        nota_final = dict['nota_final'])
    db.session.add(novoAluno)
    db.session.commit()

def updateAlunoById(id_aluno, dict):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    
    if dict.get('nome') is not None:
        aluno.nome = dict['nome'] 
    if dict.get('idade') is not None:
        aluno.idade = dict['idade']
    if dict.get('turma') is not None:
        turma = getTurmaById(dict['turma'])
        if not turma:
            raise TurmaNaoEncontrada
        aluno.turma = dict['turma']
    if dict.get('data_nascimento') is not None:
        aluno.data_nascimento = dict['data_nascimento']
    if dict.get('nota_primeiroSemestre') is not None:
        aluno.nota_primeiroSemestre = dict['nota_primeiroSemestre']
    if dict.get('nota_segundoSemestre') is not None:
        aluno.nota_segundoSemestre = dict['nota_segundoSemestre']
    if dict.get('nota_final') is not None:
        aluno.nota_final = dict['nota_final']
    
    db.session.commit()
    
def excluir_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    db.session.delete(aluno)
    db.session.commit()
