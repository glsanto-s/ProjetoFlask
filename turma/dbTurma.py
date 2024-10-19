from config import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100))
    professor = db.Column(db.Integer, unique=True)
    ativo = db.Column(db.String(100))

    def __init__(self , descricao , professor, ativo):
        self.descricao = descricao
        self.professor = professor
        self.ativo = ativo

    def to_dict(self):
        return {'id': self.id, 'descricao': self.descricao, 'professor': self.professor, 'ativo': self.ativo}