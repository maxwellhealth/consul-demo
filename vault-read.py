import requests
import json
import sys

def base_url(port):
    return 'http://127.0.0.1:' + port + '/v1/'

def read_vault_key(port, token, key):
    headers = {'X-Vault-Token': token}
    return requests.get(base_url(port) + key, headers=headers)

def main():
    try:
        port = sys.argv[1]
        token = sys.argv[2]
        key = sys.argv[3]
    except IndexError as e:
        print('Usage: ./vault-read.py port token key')
        exit(1)

    response = json.loads(read_vault_key(port, token, key).text)
    print(response['data'])

    return

if __name__ == "__main__":
    main()
