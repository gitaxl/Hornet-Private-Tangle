import os
import iota_client
LOCAL_NODE_URL = "http://0.0.0.0:14265"
client = iota_client.Client(
    nodes_name_password=[[LOCAL_NODE_URL]], node_sync_disabled=True)
    
# Get the seed from environment variable
IOTA_SEED_SECRET ='4d29c1adaf381baad88b4280f48d48d4f2dadfcace7058873a67dcd076102691' #working!'b3d7092195c36d47133ff786d4b0a1ef2ee6a0052f6e87b6dc337935c70c531e'


#client = iota_client.Client()

address_changed_list = client.get_addresses(
    seed=IOTA_SEED_SECRET,
    account_index=0,
    input_range_begin=0,
    input_range_end=10,
    get_all=True
)
print(address_changed_list)