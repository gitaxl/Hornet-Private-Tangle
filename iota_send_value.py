import iota_client
import secret

SEED = secret.Seed

NODE_URL = 'http://0.0.0.0:14265'
client = iota_client.Client(nodes_name_password=[[NODE_URL]], node_sync_disabled=True)

#USE THIS TO ACCESS DEVNET
#client = iota_client.Client()

transaction = client.message(
    seed=SEED,
    outputs=[
        {
            'address' : 'atoipt1qpme0cy0kjhll4fdu8npxld5623zd0rfq3nvvftpgdzy6qxdsw3tvhk5ue7',
            'amount' : 1_000_000,
            
        }
    ]
)
print(message)