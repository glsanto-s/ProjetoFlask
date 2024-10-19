from flask import Blueprint, request, jsonify
from .model import *

turma_blueprint = Blueprint('turmas', __name__ )

@turma_blueprint.route('/turmas', methods=['GET'])
def getTurma():
    return jsonify(getListTurma())

@turma_blueprint.route('/turma/<int:idTurma>', methods=['GET'])
def buscarTurma(idTurma):
    try:
        Turma = getTurmaById(idTurma)
        return jsonify(Turma)
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não localizada na base!'}),404
    
@turma_blueprint.route('/turma',methods=['POST'])
def adicionarTurma():
    try: 
        data = request.json
        addTurma(data)
        return jsonify(data), 201
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não localizado na base!'}),404

@turma_blueprint.route('/turma/<int:idTurma>', methods= ['PUT'])
def updateTurma(idTurma):
    data = request.json
    try:
        atualizacaoTurmaById(idTurma,data)
        return jsonify(getTurmaById(idTurma))
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não lozalizada na base!'}), 404
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não localizado na base!'}), 404
                        
@turma_blueprint.route('/turma/<int:idTurma>', methods=['DELETE'])
def deleteTurma(idTurma):
    try:
        excluirTurmaById(idTurma)
        return'', 204
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não localizada na base!'}), 404

