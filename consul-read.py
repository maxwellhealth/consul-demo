import requests
import json
import sys

def get_vault_master(port):
    r = requests.get('http://127.0.0.1:' + port + '/v1/catalog/service/vault')
    if r.status_code == requests.codes.ok:
        for node in json.loads(r.text):
            if 'active' in node['ServiceTags']:
                return node['ServiceAddress']
    else:
        return "{'Oops!'}"

def get_services(port):
    r = requests.get('http://127.0.0.1:' + port + '/v1/catalog/services')
    if r.status_code == requests.codes.ok:
        return json.loads(r.text)
    else:
        return "{'Oops!'}"

def get_nodes(port):
    r = requests.get('http://127.0.0.1:' + port + '/v1/catalog/nodes')
    if r.status_code == requests.codes.ok:
        return json.loads(r.text)
    else:
        return "{'Oops!'}"

def main():
    port = str(sys.argv[1])
    print(json.dumps(get_nodes(port), indent=4))
    print(json.dumps(get_services(port), indent=4))
    print(get_vault_master(port))
    return

if __name__ == "__main__":
    main()
