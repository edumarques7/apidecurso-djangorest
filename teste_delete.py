import requests

headers = {'Authorization': 'Token 6f5228ec34ab80b5971258c1e6ce90636b79c631'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}8/', headers=headers)

#testando codigo HTTP

assert resultado.status_code == 204
print(resultado.text)

#testando se o tamanho do conteudo é 0
assert len(resultado.text) == 0