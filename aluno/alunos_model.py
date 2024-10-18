from dbAluno import aluno
from config import db

class AlunoNaoEncontrado(Exception):
    pass

def getAlunoByid(id_aluno):
    lista_alunos = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    return aluno.to_dict()

def getlistarAlunos():
    aluno = Aluno.query.all()
    return [aluno.to_dict() for aluno in aluno]

def adicionar_aluno(dict):
    novoAluno = Aluno(nome = dict['nome'], idade = dict['idade'], turma = dict['turma'], data_nascimento = dict['data_nascimento'], nota_primeiroSemestre = dict['nota_primeiroSemestre'], nota_segundoSemestre = dict['nota_segundoSemestre'], nota_final = dict['nota_final'])
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
        aluno.turma = dict['turma']
    if dict.get('data_nascimento') is not None:
        aluno.data_nascimento = dict['data_nascimento']
    if dict.get('nota_primeiroSemestre') is not None:
        aluno.nota_primeiroSemestre = dict['nota_primeiroSemestre']
    if dict.get('nota_segundoSemestre') is not None:
        aluno.nota_segundoSemestre = dict['nota_segundoSemestre']
    if dict.get('nota_final') is not None:
        aluno.nota_final = dict['nota_final']
    
def excluir_aluno(id_aluno):
    aluno = getAlunoByid(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    db.session.delete(aluno)
    db.session.commit()
