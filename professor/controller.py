from flask import Blueprint, request, jsonify, render_template,redirect, url_for
from .model import *

professores_blueprint = Blueprint('professores', __name__)

@professores_blueprint.route('/', methods=['GET'])
def getIndex():
    return render_template('index.html')

@professores_blueprint.route('/professores', methods=['GET'])
def getProfessor():
    professores = getListProfessor()
    return render_template('professores.html', professores=professores)

@professores_blueprint.route('/professor/<int:idProfessor>', methods=['GET'])
def buscarProfessor(idProfessor):
    try:
        professor = getProfessorById(idProfessor)
        return render_template('professor_id.html',professor=professor)
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não localizado na base!'}), 404
    
@professores_blueprint.route('/professor/adicionar', methods=['GET'])
def adicionarProfessorPage():
    return render_template('professor_criar.html')   
    
@professores_blueprint.route('/professor', methods=['POST'])
def adicionarProfessor():
    nome = request.form['nome']
    idade = request.form['idade']
    materia = request.form['materia']
    observacoes = request.form['observacoes']
    data = {
        'nome':nome,
        'idade':idade,
        'materia':materia,
        'observacoes':observacoes
    }
    addProfessor(data)
    return getProfessor()

@professores_blueprint.route('/professor/<int:idProfessor>/alterar', methods=['POST'])
def updateProfessorPage(idProfessor):
    try:
        professor = getProfessorById(idProfessor)
        return render_template('professor_editar.html', professor=professor)
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não localizado na base!'}), 404

@professores_blueprint.route('/professor/<int:idProfessor>', methods=['PUT', 'POST'])
def updateProfessor(idProfessor):
    try:
        nome = request.form['nome']
        idade = request.form['idade']
        materia = request.form['materia']
        observacoes = request.form['observacoes']
        data = {
            'nome':nome,
            'idade':idade,
            'materia':materia,
            'observacoes':observacoes
        }
        updateProfessorById(idProfessor,data)
        return getProfessor()
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não localizado na base!'}), 404

@professores_blueprint.route('/professor/deletar/<int:idProfessor>', methods=['DELETE','POST'])
def deleteProfessor(idProfessor):
    try:
        deleteProfessorById(idProfessor)
        return getProfessor()
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não localizado na base!'}), 404