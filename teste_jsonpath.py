import requests
import jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes')


nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')

print(nomes)
