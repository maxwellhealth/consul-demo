# consul-demo

Contains demo scripts and examples for using consul

## Usage

Written for Python 3. `pip install -r ./requirements.txt` to grab the Requests package.

All scripts take a port as an argument but point to 127.0.0.1, so consul and vault ports will need to be forwarded over ssh.

Vault also requires a client token as an input parameter. Export it so it's easier to input in commands.

Example: `python ./vault-read 8201 ${VAULT_TOKEN} secret/foo`

## Port forwarding

### Vault

The Vault HA pair is currently only reachable from the consul-seed server, therefore to access vault over localhost, you'll need to forward port 8200 from the vault server to the consul-seed server to your local machine (if that's where you're running the scripts). Forwarding 8200 from both Vault servers to 8200 on the ssh client will result in a conflict, so it is recommended to reassign port numbers according to which instance you plan to call, as shown below

### Consul 

Same deal for consul, but you don't need to forward through an extra box if you don't want to. Just forward 8500. 

Example ssh config on your local machine:
```
host consul-seed
  Hostname 12.34.56.78
  User ubuntu
  IdentityFile ~/.ssh/a_key_that_works.pem
  ForwardAgent yes
  LocalForward 8500 127.0.0.1:8500
  LocalForward 8501 127.0.0.1:8501 # Consul UI on Vault1
  LocalForward 8502 127.0.0.1:8502 # Consul UI on Vault2
  LocalForward 8201 127.0.0.1:8201 # Vault API on Vault1
  LocalForward 8202 127.0.0.1:8202 # Vault API on Vault2
```

And on the consul-seed server:
```
Host vault1
  Hostname 1.2.3.4
  LocalForward 8501 127.0.0.1:8500
  LocalForward 8201 127.0.0.1:8200

Host vault2
  Hostname 5.6.7.8
  LocalForward 8502 127.0.0.1:8500
  LocalForward 8202 127.0.0.1:8200
```
