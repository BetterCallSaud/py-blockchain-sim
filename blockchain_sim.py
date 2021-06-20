"""
@Author: Saud Hashmi
@Date Created: 20/06/2021
@Title: Blockchain Simulator
"""

# Importing modules
import hashlib                 #hashlib for hashing algorithms
import datetime as date        #datetime for dates

class Block():
    def __init__(self, height, timestamp, data, prev_hash):
        self.height = height
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hash_block()

    def hash_block(self):
        msg = (str(self.height) + str(self.timestamp) + str(self.data) + str(self.prev_hash)).encode()
        sha = hashlib.sha256(msg)
        return sha.hexdigest()

def create_genesis_block():
    # Manually construct a block with height zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    this_height = last_block.height + 1
    this_timestamp = date.datetime.now()
    this_data = "Hello. I am Block #" + str(this_height)
    this_hash = last_block.hash
    return Block(this_height, this_timestamp, this_data, this_hash)

if __name__=="__main__":
    
    # Create blockchain and add the genesis block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    # Let's add 20 blocks to the chain
    blocknum = 20

    # We will be mining 20 blocks
    for i in range(1, blocknum+1):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add

        # Showing block information
        print(f"Block #{i} has been added to the blockchain!")
        print(f"Hash: {block_to_add.hash}")
        print(f"Block Height: {block_to_add.height}")