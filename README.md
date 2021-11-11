# Hornet-Private-Tangle
#Running your own Private Tangle on localhost

    Use iota_gen_seed.py to generate a random seed 

    Copy your seed 

    Use iota_generate_addr.py to generate addresses from your seed 

    Copy Hex 64 address 

    Open private-tangle.sh in your editor 

    Navigate to line 194  

    Replace $(cat ../../address.txt) with your Hex 64 address 

    Install your Private Tangle as usual 

    --
    Create a file named secret.py and create a variable named "Seed" with value of your previously generated seed
    Send tokens with iota_sendtkns.py 
