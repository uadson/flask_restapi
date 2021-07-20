import requests
import json

response_get = requests.get('http://127.0.0.1:5000/values')

dados = response_get.json()
print(dados)
print(f"Total Sum is: {dados['total_sum']}")

response_post = requests.post('http://127.0.0.1:5000/values', json={'values': [10, 20, 30, 40]})

dados = response_post.json()
print(dados)
print(f"Total Sum is: {dados['total_sum']}")