from flask import Blueprint, request, jsonify
from .alunos_model import *

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = listar_alunos()
    return render_template("alunos.html", alunos=alunos)

@alunos_blueprint.route('/aluno/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
    try:
        aluno = getAlunoByid(id_aluno)
        nome = request.form['nome']
        aluno_data = {'nome': nome}
        atualizar_aluno(id_aluno, aluno_data)
        return redirect(url_for('alunos.get_aluno', id_aluno=id_aluno))
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404
    

@alunos_blueprint.route('/aluno', methods=['POST'])
def create_aluno():
    try:
        nome = request.form['nome']
        novo_aluno = {'nome': nome}
        adicionar_aluno(novo_aluno)
        return redirect(url_for('alunos.get_alunos')), 201
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
        return redirect(url_for('alunos.get_alunos')), 204
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404