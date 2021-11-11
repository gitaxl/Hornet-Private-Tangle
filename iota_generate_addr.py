import iota_client
import secret

SEED = secret.Seed

if not SEED:
    raise Exception("Check your secret!")


NODE_URL = 'http://0.0.0.0:14265'
client = iota_client.Client(nodes_name_password=[[NODE_URL]], node_sync_disabled=True)

# USE THIS TO ACCESS DEVNET
#client = iota_client.Client()

address_changed_list = client.get_addresses(
    seed=SEED,
    account_index=0,
    input_range_begin=0,
    input_range_end=10,
    get_all=False
)
a = address_changed_list[0][0]
print(f' Bech32 = {a}')
b = client.bech32_to_hex(a)
print(f' Hex_64 = {b}')