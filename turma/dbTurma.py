from config import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100))
    professor = db.Column(db.String(100))
    ativo = db.Column(db.String(100))

    def __init__(self, id , descricao , professor, ativo):
        self.id = id
        self.descricao = descricao
        self.professor = professor
        self.ativo = ativo

    def to_dict(self):
        return {'id': self.id, 'descricao': self.descricao, 'professor': self.professor, 'ativo': self.ativo}