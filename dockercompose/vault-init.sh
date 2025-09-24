#!/bin/sh

set -e

export VAULT_ADDR=http://vault:8200

# give some time for Vault to start and be ready
sleep 5

# login with root token at $VAULT_ADDR
vault login root

# enable the KV secrets engine at the default path (demo/)
vault secrets enable -path=demo -version=2 kv

# write a secret to the kv store
vault kv put demo/mysql/user username="admin" password="dummy"

# read the secret back
vault kv get demo/mysql/user

# create policy to read secret
vault policy write myapp-policy myapp-policy.hcl