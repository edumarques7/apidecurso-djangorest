import requests

headers = {'Authorization': 'Token 6f5228ec34ab80b5971258c1e6ce90636b79c631'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "curso projetos cffom scrujm",
    "url": "https://www.lddinudxgguf6ufmj.com"

}


resultado = requests.post(url='http://localhost:8000/api/v2/cursos/', headers=headers, data=novo_curso)

# Testando o codigo de status HTTP
assert resultado.status_code == 201

# Testando se o  titulo do curso é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']