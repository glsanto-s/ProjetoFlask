from flask import Blueprint, request, jsonify
from .alunos_model import *

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(getlistarAlunos())

@alunos_blueprint.route('/aluno/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
    try:
        aluno = getAlunoByid(id_aluno)
        return jsonify(aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404
    

@alunos_blueprint.route('/aluno', methods=['POST'])
def create_aluno():
    try: 
        data = request.json
        adicionar_aluno(data)
        return jsonify(data), 201
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não localizada na base!'}),404

@alunos_blueprint.route('/aluno/<int:id_aluno>', methods=['PUT'])
def atualizar_aluno(id_aluno):
    data = request.json
    try:
        updateAlunoById(id_aluno, data)
        return jsonify(getAlunoByid(id_aluno))
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não localizada na base!'}),404

@alunos_blueprint.route('/aluno/<int:id_aluno>', methods=['DELETE'])
def delete_aluno(id_aluno):
    try:
        excluir_aluno(id_aluno)
        return '', 204
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404