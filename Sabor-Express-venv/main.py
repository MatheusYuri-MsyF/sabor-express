from fastapi import FastAPI, Query
import requests

app = FastAPI()


@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    """
    Endpoint para buscar informações sobre restaurantes.

    Este endpoint permite buscar todos os restaurantes ou um restaurante específico.

    Args:
        restaurante (str, optional): Nome do restaurante a ser buscado. Defaults to None.

    Returns:
        dict: Um dicionário contendo os dados dos restaurantes, ou uma mensagem de erro.
    """
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    '''
    Endpoint para exibir cardapios!
    '''
    if response.status_code == 200:
        # A requisição à API foi bem-sucedida
        dados_json = response.json()
        if restaurante is None:
            # Retorna todos os dados dos restaurantes
            return {'Dados':dados_json}
        # Filtra os dados para encontrar o restaurante específico
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                "item": item['Item'],
                "price": item['price'], 
                "description": item['description']})
        return {'Restaurante':restaurante, 'Cardapio':dados_restaurante}    
    else:
        # Houve um erro na requisição à API
        return {'Erro':f'{response.status_code} - {response.text}'}
