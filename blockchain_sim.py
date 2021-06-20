"""
@Author: Saud Hashmi
@Date Created: 20/06/2021
@Title: Blockchain Simulator
"""

# Importing modules
import hashlib                 # hashlib for hashing algorithms
import datetime as date        # datetime for dates
import random                  # random for randomizing numbers for transactions 
# import math                    # math for logarithmic function used in merkle root hashing function              

class Block():
    """
        A certain block consists of the following entities:
        + Block height
        + Timestamp
        + Previous block hash
        + Transactions
        + Transactions counter
    """
    def __init__(self, height, timestamp, prev_hash, txs):
        self.height = height
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.hash = self.hash_block()
        self.transactions = txs
        self.tx_ctr = len(txs)
        # self.merkle = self.merkel_root_hash(self.tx_ctr)

    def hash_block(self):
        msg = (str(self.height) + str(self.timestamp) + str(self.prev_hash)).encode()
        sha = hashlib.sha256(msg)
        return sha.hexdigest()

    # def merkel_root_hash():
    #     pass

def create_genesis_block():
    # Manually construct a block with height zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "0", [random.randint(1,1000) for _ in range(10)])

def next_block(last_block):
    this_height = last_block.height + 1
    this_timestamp = date.datetime.now()
    this_hash = last_block.hash
    this_txs = [random.randint(1,1000) for _ in range(10)]
    return Block(this_height, this_timestamp, this_hash, this_txs)

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
        print(
            (f"\nBlock #{i} has been added to the blockchain!\n"),
            ("\t\t{}\n".format("_"*100)),
            (f"\t\tHash: {block_to_add.hash}"),
            (f"| Block Height: {block_to_add.height}"),
            (f"| Timestamp: {block_to_add.timestamp}"),
            (f"| Previous Root Hash: {block_to_add.prev_hash}"),
            (f"| Transactions: {block_to_add.transactions}"),
            (f"| Transaction Counter: {block_to_add.tx_ctr}"),
            ("\t\t{}\n".format("_"*100))
        )