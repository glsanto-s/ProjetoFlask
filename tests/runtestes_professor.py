import unittest
import requests

localhost = 'http://127.0.0.1:8000/'

class TestProfessorEndpoints(unittest.TestCase):
    
    def test_000_professor_retorna_lista(self):
        res = requests.get(f'{localhost}professores')
        if res.status_code == 404:
            self.fail("Você não definiu a página /professores no seu server")
        
        self.assertEqual(res.status_code,200,"Falha ao buscar lista de Professores")
        
        self.assertIn('text/html', res.headers['Content-Type'], "Esperava resposta HTML para a lista de professores")
        self.assertIn('<h1>Lista de Professores</h1>', res.text, "Conteúdo HTML esperado não encontrado na resposta")
        
    def test_001_professor_por_id_encontrado(self):
        idProfessor = 13
        res = requests.get(f'{localhost}professor/{idProfessor}')
        
        self.assertEqual(res.status_code,200,"Falha ao buscar professor")
        
        self.assertIn('<h1>Detalhes do Professor</h1>', res.text, "Conteúdo HTML esperado não encontrado na resposta")
    
    def test_002_professor_por_id_nao_encontrado(self):
        idProfessor = 123
        res = requests.get(f'{localhost}professor/{idProfessor}')
        
        self.assertEqual(res.status_code,404,"Deveria retornar 404 quando o professor não é encontrado")
        
        json_data = res.json()
        self.assertEqual(json_data['message'], 'Professor não localizado na base!', "Mensagem de erro inesperada.")
    
    def test_003_professor_adicionar_pagina(self):
        res = requests.get(f'{localhost}professor/adicionar')
        
        if res.status_code == 404:
            self.fail("Você não definiu a página /professores/adicionar no seu server")
            
        self.assertEqual(res.status_code,200,"Falha ao buscar página adicionar professor")
        
        self.assertIn('text/html', res.headers['Content-Type'], "Esperava resposta HTML para a adicionar professor")
        self.assertIn('<h2>Adicionar Professor</h2>', res.text, "Conteúdo HTML esperado não encontrado na resposta")
    
    def test_004_professor_adicionar_sucesso(self):
        data = {
            'nome':'Gyovanna',
            'idade':20,
            'materia':'ADS',
            'observacoes':'Teste'
        }
        
        res = requests.post(f'{localhost}professor', data=data)
        
        self.assertEqual(res.status_code,200,"Falha ao adicionar professor")
        self.assertIn('text/html', res.headers['Content-Type'], "Esperava resposta HTML para a lista de professores.")
        self.assertIn('<h1>Lista de Professores</h1>', res.text, "Conteúdo HTML esperado não encontrado na resposta final.")
        
    def test_005_professor_alterar_pagina_sucesso(self):
        idProfessor = 6
        res = requests.post(f'{localhost}professor/{idProfessor}/alterar')
            
        self.assertEqual(res.status_code,200,"Falha ao buscar página alterar professor")
        
        self.assertIn('text/html', res.headers['Content-Type'], "Esperava resposta HTML para a adicionar professor")
        self.assertIn('<h2>Atualizar Professor</h2>', res.text, "Conteúdo HTML esperado não encontrado na resposta")
    
    def test_006_professor_alterar_pagina_nao_encontrado(self):
        idProfessor = 123
        res = requests.post(f'{localhost}professor/{idProfessor}/alterar')
        
        self.assertEqual(res.status_code,404,"Deveria retornar 404 quando professor não é encontrado")
        json_data = res.json()
        self.assertEqual(json_data['message'], 'Professor não localizado na base!', "Mensagem de erro inesperada.")
    
    def test_007_professor_alterar_sucesso(self):
        data = {
            'nome':'Gyovanna',
            'idade':20,
            'materia':'ADS',
            'observacoes':'aaaaa'
        }
        
        idProfessor = 6
        res = requests.post(f'{localhost}professor/{idProfessor}', data=data)
        self.assertEqual(res.status_code, 200, "Falha ao atualizar o professor.")
        
        self.assertIn('text/html', res.headers['Content-Type'], "Esperava resposta HTML para a lista de professores.")
        self.assertIn('<h1>Lista de Professores</h1>', res.text, "Conteúdo HTML esperado não encontrado na resposta final.")
    
    def test_008_professor_alterar_nao_encontrado(self):
        data = {
            'nome':'Gyovanna',
            'idade':20,
            'materia':'ADS',
            'observacoes':'Teste'
        }
        
        idProfessor = 756
        res = requests.put(f'{localhost}professor/{idProfessor}', data=data)
        self.assertEqual(res.status_code, 404, "Deveria retornar 404 quando professor não é encontrado")
        
        json_data = res.json()
        self.assertIn('message', json_data, "Mensagem de erro não encontrada.")
        self.assertEqual(json_data['message'], 'Professor não localizado na base!', "Mensagem de erro incorreta para professor não encontrado.")
    
    def test_009_professor_deletar_sucesso(self):
        idProfessor = 17
        res = requests.post(f'{localhost}professor/deletar/{idProfessor}')
        self.assertEqual(res.status_code, 200, "Falha ao excluir o professor.")

        res = requests.get('{localhost}professores')
        self.assertEqual(res.status_code, 200, "Falha ao carregar a página de professores após redirecionamento.")
        
        self.assertIn('text/html', res.headers['Content-Type'], "Esperava resposta HTML para a lista de professores.")
        self.assertIn('<h1>Lista de Professores</h1>', res.text, "Conteúdo HTML esperado não encontrado na resposta final.")
        
    def test_010_professor_deletar_nao_encontrado(self):
        id_professor = 963
        response = requests.delete(f'{localhost}professor/deletar/{id_professor}')
        
        self.assertEqual(response.status_code, 404, "Deveria retornar 404 quando o professor não é encontrado.")
        
        json_data = response.json()
        self.assertIn('message', json_data, "Mensagem de erro não encontrada.")
        self.assertEqual(json_data['message'], 'Professor não localizado na base!', "Mensagem de erro incorreta para professor não encontrado.")


if __name__ == '__main__':
    unittest.main()
