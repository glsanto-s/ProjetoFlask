from flask import Blueprint, request, jsonify, render_template, url_for, redirect
from .alunos_model import *

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/', methods=['GET'])
def getIndex():
    return render_template('index.html')

@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = getlistarAlunos()
    return render_template("alunos.html", alunos=alunos)

@alunos_blueprint.route('/aluno/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
    try:
        aluno = getAlunoByid(id_aluno)
        return render_template('aluno_id.html', aluno=aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

@alunos_blueprint.route('/aluno/adicionar', methods=['GET'])
def adicionarAlunoPage():
    return render_template('criarAlunos.html')

@alunos_blueprint.route('/aluno', methods=['POST'])
def create_aluno():
    try:
        nome = request.form['nome']
        idade = request.form['idade']
        turma = request.form['turma']
        data_nascimento = request.form['data_nascimento']
        nota_primeiroSemestre = request.form['nota_primeiroSemestre']
        nota_segundoSemestre = request.form['nota_segundoSemestre']
        nota_final = request.form['nota_final']
        data = {
            'nome': nome,
            'idade': idade,
            'turma': turma,
            'data_nascimento': data_nascimento,
            'nota_primeiroSemestre': nota_primeiroSemestre,
            'nota_segundoSemestre': nota_segundoSemestre,
            'nota_final': nota_final
        }
        adicionar_aluno(data)
        return get_alunos()
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não localizada na base!'}), 404
    
@alunos_blueprint.route('/aluno/<int:id_aluno>/alterar', methods=['POST'])
def atualizarAlunoPage(id_aluno):
    try:
        aluno = getAlunoByid(id_aluno)
        return render_template('aluno_update.html', aluno=aluno)
    except AlunoNaoEncontrado:
         return jsonify({'message': 'Aluno não encontrado'}), 404

@alunos_blueprint.route('/aluno/<int:id_aluno>', methods=['PUT','POST'])
def atualizar_aluno(id_aluno):
    try:
        nome = request.form['nome']
        idade = request.form['idade']
        turma = request.form['turma']
        data_nascimento = request.form['data_nascimento']
        nota_primeiroSemestre = request.form['nota_primeiroSemestre']
        nota_segundoSemestre = request.form['nota_segundoSemestre']
        nota_final = request.form['nota_final']
        data = {
            'nome': nome,
            'idade': idade,
            'turma': turma,
            'data_nascimento': data_nascimento,
            'nota_primeiroSemestre': nota_primeiroSemestre,
            'nota_segundoSemestre': nota_segundoSemestre,
            'nota_final': nota_final
        }
        updateAlunoById(id_aluno, data)
        return get_alunos()

    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não localizada na base!'}),404

@alunos_blueprint.route('/aluno/deletar/<int:id_aluno>', methods=['DELETE', 'POST'])
def delete_aluno(id_aluno):
    try:
        excluir_aluno(id_aluno)
        return get_alunos()
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404