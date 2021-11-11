
import iota_client
import secret

SEED = secret.Seed

#Connect to Iota Devnet with uncommenting line 5 and commenting lines 6-8 off
#client = iota_client.Client()

LOCAL_NODE_URL = "http://0.0.0.0:14265"
client = iota_client.Client(
    nodes_name_password=[[LOCAL_NODE_URL]], node_sync_disabled=True)

message = client.message(
    seed = SEED,
    outputs=[
        {   #replace "atoi..." with your atoi address
            'address' : 'atoi...',
            'amount' : 1_000_000
        }
    ]
)


print(message)
