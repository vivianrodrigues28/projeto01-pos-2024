from flask import Flask, redirect, request, session, url_for
from authlib.integrations.flask_client import OAuth
import requests

app = Flask(__name__)
app.secret_key = 'development'  
oauth = OAuth(app)


oauth.register(
    name='suap',
    client_id='',
    client_secret='',
    api_base_url='https://suap.ifrn.edu.br/api/', 
    authorize_url='https://suap.ifrn.edu.br/o/authorize/',
    access_token_url='https://suap.ifrn.edu.br/o/token/',  
    client_kwargs={'scope': 'read'},
    fetch_token=lambda: session.get('suap_token')
)


@app.route('/')
def index():
    if 'suap_token' in session: 
        token = session['suap_token']
        headers = {'Authorization': f'Bearer {token["access_token"]}'}
        profile_response = requests.get('https://suap.ifrn.edu.br/api/minhas-informacoes/meus-dados/', headers=headers)
        profile = profile_response.json()
        return f"Olá, {profile['nome_completo']}!"  
    else:
        return redirect(url_for('login'))


@app.route('/login')
def login():
    redirect_uri = url_for('callback', _external=True)
    return oauth.suap.authorize_redirect(redirect_uri)


@app.route('/callback')
def callback():
    token = oauth.suap.authorize_access_token() 
    session['suap_token'] = token  
    return redirect(url_for('index'))  


@app.route('/boletins')
def boletins():
    if 'suap_token' in session:
        token = session['suap_token']
        headers = {'Authorization': f'Bearer {token["access_token"]}'}
        
       
        year = request.args.get('year')
        semester = request.args.get('semester')
        
       
        boletins_url = f'https://suap.ifrn.edu.br/api/minhas-informacoes/boletim/{year}/{semester}/'
        boletins_response = requests.get(boletins_url, headers=headers)
        boletins = boletins_response.json()
        
        return boletins
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
