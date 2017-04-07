import requests
import json
import sys
from base64 import b64decode

def write_key(port, key, value):
    '''
    Key writes happen by sending a PUT to the consul agent
    Data field must contain the data you wish to add.
    It does not have to be json-ized.
    Data will be b64 encoded upon receipt
    
    Returns true if write was successful
    '''

    r = requests.put('http://127.0.0.1:' + port + '/v1/kv/' + key, data = value)
    return r.text

def read_key(port, key):
    '''
    Data can be read by sending a GET to the consul agent. 
    Notice that the write and read operation use the same endpoint.

    Data back as a JSON object (lol, mostly) 
    '''
    r = requests.get('http://127.0.1:' + port + '/v1/kv/' + key)
    data = json.loads(r.text)

    # wtf, guys? it's a one-item list inside the object?
    # The returned object actually has a few fields,
    # but we only care about 'Value' today
    return b64decode(data[0]['Value'])

def main():
    '''
    Use consul UI to view and set keys to start the lab.
    Consul UI can be reached by forwarding port 8500
    from one of the two vault servers through consul-seed
    and to your local machine.
    Example URL: http://127.0.0.1:8500/ui/#/dc1/services

    Set key "foo" with a value of "bar" to run this lab
    '''

    port = sys.argv[1]

    # Expect 'bar'
    print(read_key(port, key='foo'))

    # Write 'baz', expect 'True'
    print(write_key(port, key='foo', value='baz'))

    # Expect 'foo'
    print(read_key(port, key='foo'))
    return

if __name__ == "__main__":
    main()
