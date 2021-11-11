
import iota_client
import secret

LOCAL_NODE_URL = "http://0.0.0.0:14265"
client = iota_client.Client(
    nodes_name_password=[[LOCAL_NODE_URL]], node_sync_disabled=True)


IOTA_SEED_SECRET = secret.SEED
#client = iota_client.Client()

message = client.message(
    seed = IOTA_SEED_SECRET,
    outputs=[
        {   #replace "atoi..." with your atoi address
            'address' : 'atoi...',
            'amount' : 666_666_666
        }
    ]
)


print(message)
