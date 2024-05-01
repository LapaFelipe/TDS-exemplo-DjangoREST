import requests

def get_dados():
    response = requests.get('http://localhost:8000/api/produto/')
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_dado(id):
    response = requests.get(f'http://localhost:8000/api/produto/{id}')
    if response.status_code == 200:
        return response.json()
    else:
        return None

def create_dado(novo_dado):
    response = requests.post('http://localhost:8000/api/produto/', json=novo_dado)
    if response.status_code == 201:
        return response.json()
    else:
        return None

def update_dado(id, dados_atualizados):
    url = f'http://localhost:8000/api/produto/{id}/'
    response = requests.put(url, json=dados_atualizados)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def delete_dado(id):
    url = f'http://localhost:8000/api/produto/{id}/'
    response = requests.delete(url)
    return response.status_code