
import os
import requests

VAULT_HOST = os.environ.get('VAULT_HOST', 'https://vault-beta.daumkakao.io/v1')


def get_vault_secrets(key, token):
    url = f'{VAULT_HOST}/{key}'

    try:
        res = requests.get(url, headers={'X-Vault-Token': token})
        if res.status_code == 200:
            return res.json()['data']
        else:
            return None
    except Exception as e:
        raise
