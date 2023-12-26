import requests

headers = {'Authorization': 'Token 6f5228ec34ab80b5971258c1e6ce90636b79c631'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes'

curso_atualizado = {
    "titulo": "Novo curso scrum 000",
    "url": "http://scrum33.com.br"
}

# Buscando url do curso ID 15
# curso = requests.get(url='http://localhost:8000/api/v2/cursos/15', headers=headers)

#print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}7/', headers=headers, data=curso_atualizado)
print()

assert resultado.status_code == 200

assert resultado.json()['titulo'] == curso_atualizado['titulo']