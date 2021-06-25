
import os
import requests
import json

from typing import Any

VAULT_HOST = os.environ.get('VAULT_HOST', 'https://vault-beta.daumkakao.io/v1')
VAULT_FILE = 'vault'


def get_vault_secrets(key: str, token: str):
    url = f'{VAULT_HOST}/{key}'

    try:
        res = requests.get(url, headers={'X-Vault-Token': token})
        if res.status_code == 200:
            return res.json()['data']
        else:
            return {}
    except Exception as e:
        raise


def load_vault_secrets_from_vault_file(key: Any = None):
    try:
        with open(VAULT_FILE, 'r') as f:
            ret = json.load(f)
    except Exception as e:
        ret = {}

    if key is not None:
        return ret.get(key, {})

    return ret


def save_vault_secrets_to_vault_file(vault_data: dict, key: Any):
    new_data = load_vault_secrets_from_vault_file()

    new_data[key] = vault_data

    with open(VAULT_FILE, 'w') as f:
        f.write(json.dumps(new_data))
