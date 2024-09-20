import requests

class SuapClient:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = 'https://suap.ifrn.edu.br/api/'

    def get_user_profile(self):
        url = f'{self.base_url}minhas-informacoes/meus-dados/'
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_boletins(self, year=None, semester=None):
        url = f'{self.base_url}minhas-informacoes/boletim/'
        params = {'ano_letivo': year, 'periodo_letivo': semester}
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(url, headers=headers, params=params)
        return response.json()