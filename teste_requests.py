import requests


# GET Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes')

#Acessando o codigo status HTTP
# print(avaliacoes.status_code)


# acessando dados da resposta
print(avaliacoes.json())

# Acessando a quantidade de registos