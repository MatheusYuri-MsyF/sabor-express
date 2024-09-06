import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    # A requisição à API foi bem-sucedida
    dados_json = response.json()
    dados_restaurante = {}
    # Itera sobre cada item do JSON, agrupando os itens por restaurante
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in  dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
        "item": item ['Item'],
        "price": item['price'], 
        "description": item['description']})
else:
    # Houve um erro na requisição à API
    print(f'O erro foi {response.status_code}')
    
# Cria um arquivo JSON para cada restaurante
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
