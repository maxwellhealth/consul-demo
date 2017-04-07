import requests
import json
import sys

def base_url(port):
    return 'http://127.0.0.1:' + port + '/v1/'

def write_vault_key(port, token, key, value):
    headers = {'X-Vault-Token': token, 'Content-Type': 'application/json'}
    body = json.dumps({'value': value})
    return requests.post(base_url(port) + key, headers=headers, data=body).status_code

def main():
    try:
        port = sys.argv[1]
        token = sys.argv[2]
        key = sys.argv[3]
        value = sys.argv[4]
    except IndexError as e:
        print('Usage: ./vault-write.py port token key value')
        exit(1)
    
    if write_vault_key(port, token, key, value) == 204: # Gotta compare it to int, not string. Strong types ftw.
        print("Data written!")
    else:
        print("Computer says no")
    return

if __name__ == "__main__":
    main()
