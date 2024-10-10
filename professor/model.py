from dados import dados
dadosProfessores = dados['professores']

class ProfessorNaoEncontrado(Exception):
    pass

def getListProfessor():
    return dadosProfessores

def getProfessorById(idProfessor):
    for professor in dadosProfessores:
        if professor['id'] == idProfessor:
            return professor
    raise ProfessorNaoEncontrado

def validaProfessorExist(idProfessor):
    try:
        getProfessorById(idProfessor)
        return True
    except Exception:
        return False

def addProfessor(dict):
    dadosProfessores.append(dict)

def updateProfessorById(idProfessor, dict):
    validacao = validaProfessorExist(idProfessor)
    if validacao is True:
        for professor in dadosProfessores:
            if professor['id'] == idProfessor:
                professor.update(dict)
                break
    else:
        raise ProfessorNaoEncontrado

def deleteProfessorById(idProfessor):
    validacao = validaProfessorExist(idProfessor)
    if validacao is True:
        professor = getProfessorById(idProfessor)
        dadosProfessores.remove(professor)
    else:
        raise ProfessorNaoEncontrado