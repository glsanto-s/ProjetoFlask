from flask import Blueprint, request, jsonify, render_template,redirect, url_for
from .model import *

turma_blueprint = Blueprint('turmas', __name__ )

@turma_blueprint.route('/', methods=['GET'])
def getIndex():
    return "Meu index"

@turma_blueprint.route('/turmas', methods=['GET'])
def getTurma():
    turmas= getListTurma()
    return render_template('turmas.html', turmas=turmas)

@turma_blueprint.route('/turma/<int:idTurma>', methods=['GET'])
def buscarTurma(idTurma):
    try:
        turma = getTurmaById(idTurma)
        return render_template('turma_id.html',turma=turma)
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não localizada na base!'}),404

@turma_blueprint.route('/turma/adicionar', methods=['GET'])
def adicionarTurmaPage():
    return render_template('turma_criar.html')

@turma_blueprint.route('/turma',methods=['POST'])
def adicionarTurma():
    try:
        descricao = request.form['descricao']
        professor = request.form['professor']
        ativo = request.form ['ativo']
        data = {
            'descricao':descricao,
            'professor':professor,
            'ativo':ativo
        }
        addTurma(data)
        return getTurma()
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não localizado na base!'}),404

@turma_blueprint.route('/turma/<int:idTurma>/alterar',methods=['POST'])
def updateTurmasPage(idTurma):
    try:
        turma = getTurmaById(idTurma)
        return render_template('turma_editar.html',turma=turma)
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não localizada na base!'}), 404
    
@turma_blueprint.route('/turma/<int:idTurma>', methods= ['PUT','POST'])
def updateTurma(idTurma):
    try: 
        descricao = request.form['descricao']
        professor = request.form['professor']
        ativo = request.form ['ativo']
        data = {
            'descricao':descricao,
            'professor':professor,
            'ativo':ativo
        }
        atualizacaoTurmaById(idTurma,data)
        return jsonify(getTurmaById(idTurma))
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não lozalizada na base!'}), 404
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não localizado na base!'}), 404
                        
@turma_blueprint.route('/turma/deletar/<int:idTurma>', methods=['DELETE', 'POST'])
def deleteTurma(idTurma):
    try:
        excluirTurmaById(idTurma)
        return getTurma()
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não localizada na base!'}), 404

