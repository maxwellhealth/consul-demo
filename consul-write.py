import requests
import json
import sys
from base64 import b64decode

def write_key(port, key, value):
    r = requests.put('http://127.0.0.1:' + port + '/v1/kv/' + key, data = value)
    return r.text

def read_key(port, key):
    r = requests.get('http://127.0.1:' + port + '/v1/kv/' + key)
    return json.loads(r.text)

def main():
    port = sys.argv[1]
    key = read_key(port, key='foo')
    value = key[0]['Value']
    print(b64decode(value))

    print(write_key(port, key='foo', value='baz'))
    key = read_key(port, key='foo')
    value = key[0]['Value']
    print(b64decode(value))
    return

if __name__ == "__main__":
    main()
