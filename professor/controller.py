from flask import Blueprint, request, jsonify
from .model import *

professores_blueprint = Blueprint('professores', __name__)

@professores_blueprint.route('/professores', methods=['GET'])
def getProfessor():
    return jsonify(getListProfessor())

@professores_blueprint.route('/professor/<int:idProfessor>', methods=['GET'])
def buscarProfessor(idProfessor):
    try:
        professor = getProfessorById(idProfessor)
        return jsonify(professor)
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não localizado na base!'}), 404
    
@professores_blueprint.route('/professor', methods=['POST'])
def adicionarProfessor():
    data = request.json
    addProfessor(data)
    return jsonify(data), 201

@professores_blueprint.route('/professor/<int:idProfessor>', methods=['PUT'])
def updateProfessor(idProfessor):
    data = request.json
    try:
        updateProfessorById(idProfessor,data)
        return jsonify(getProfessorById(idProfessor))
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não localizado na base!'}), 404

@professores_blueprint.route('/professor/<int:idProfessor>', methods=['DELETE'])
def deleteProfessor(idProfessor):
    try:
        deleteProfessorById(idProfessor)
        return '', 204
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não localizado na base!'}), 404