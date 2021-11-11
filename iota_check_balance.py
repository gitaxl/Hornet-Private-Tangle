import iota_client
import secret

NODE_URL = "http://0.0.0.0:14265"
# NODE_URL = 'https://api.lb-0.h.chrysalis-devnet.iota.cafe:443'

SEED = secret.Seed
#ADDRESS = Address you want to check


client = iota_client.Client(
    nodes_name_password=[[NODE_URL]], node_sync_disabled=True)

# Status of the Network
print(f'node_info: {client.get_info()}')

# Get balance of entire Seed
print(f'balance of SEED: {client.get_balance(seed=SEED)}')

# Get balance of a single address BECH32(iota/atoi...)
print(client.get_address_balance(ADDRESS))