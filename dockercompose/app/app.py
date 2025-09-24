# app.py
from flask import Flask, render_template
import hvac
import os

app = Flask(__name__, template_folder='.')

# Inicializa el cliente de Vault
vault_url = os.environ.get('VAULT_URL', 'http://192.168.1.237:8200')
vault_token = os.environ.get('VAULT_TOKEN', 'token')
client = hvac.Client(url=vault_url, token=vault_token)

@app.route('/')
def index():
    try:
        # Lee el secreto desde Vault
        response = client.secrets.kv.v2.read_secret_version(
            path='mysql/user',  # Ajusta la ruta del secreto
            mount_point='demo'  # Ajusta el punto de montaje si es necesario
        )
        # Extrae los datos del secreto
        data = response['data']['data']
        username = data.get('username', 'No encontrado')
        password = data.get('password', 'No encontrado')
    except Exception as e:
        # Muestra un mensaje de error si algo sale mal
        username = 'Error'
        password = str(e)
    
    # Renderiza el template HTML con los datos del secreto
    return render_template('index.html', username=username, password=password)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)