from config import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    turma = db.Column(db.Integer, unique=True)
    data_nascimento = db.Column(db.Integer)
    nota_primeiroSemestre = db.Column(db.Integer)
    nota_segundoSemestre = db.Column(db.Integer)
    nota_final = db.Column(db.Integer)

    def __init__(self, nome, idade, turma, data_nascimento, nota_primeiroSemestre, 
                 nota_segundoSemestre, nota_final):
        self.nome = nome
        self.idade = idade
        self.turma = turma
        self.data_nascimento = data_nascimento
        self.nota_primeiroSemestre = nota_primeiroSemestre
        self.nota_segundoSemestre = nota_segundoSemestre
        nota_final = nota_final
    
    def to_dict(self):
        return{'id':self.id, 'nome': self.nome, 'idade': self.idade, 'turma': self.turma, 'data_nascimento': self.data_nascimento, 'nota_primeiroSemestre': self.nota_primeiroSemestre, 'nota_segundoSemestre': self.nota_segundoSemestre, 'nota_final': self.nota_final}