import requests

headers = {'Authorization': 'Token b625b4dc005662628c732728365bb45d97a094b4'}

url_cursos = 'http://localhost:8000/api/v2/cursos'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes'

resultado = requests.get(url=url_cursos, headers=headers)

print(resultado.json())

assert resultado.status_code == 200