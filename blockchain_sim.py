"""
@Author: Saud Hashmi
@Date Created: 20/06/2021
@Title: Blockchain Simulator
"""

# Importing modules
import hashlib                 # hashlib for hashing algorithms
import datetime as date        # datetime for dates
import random                  # random for randomizing numbers for transactions 

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
        self.merkle = self.merkle_root_hash(self.transactions)
    #-------------------------------------------------------------------------------------
    """
    Both functions generate hash using SHA-256 algorithm
    """
    def hashing(self, s):
        s = s.encode()
        sha = hashlib.sha256(s).hexdigest()
        return sha
    #-------------------------------------------------------------------------------------
    """
    Creates hash for the block
    """
    def hash_block(self):
        s = str(self.height) + str(self.timestamp) + str(self.prev_hash)
        return self.hashing(s)
    #-------------------------------------------------------------------------------------
    """
    Generates Merkle Root Hash for all transactions
    """
    def merkle_root_hash(self, txs):
        if (len(txs) == 1):
            return txs[0]
        newtxs = []
        for i in range(0, len(txs)-1, 2):
            newtxs.append(self.hashing(str(txs[i]) + str(txs[i+1])))
        if len(txs)%2 == 1:
            newtxs.append(self.hashing(str(txs[-1]) + str(txs[-1])))
        return self.merkle_root_hash(newtxs)
    

"""
Creates the genesis block, i.e. the first block of the blockchain
"""
def create_genesis_block():
    # Manually construct a block with height zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "0", [random.randint(1,1000) for _ in range(10)])


"""
Defines properties for the next block in the blockchain
"""
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
            (f"| Merkle Root Hash: {block_to_add.merkle}"),
            ("\t\t{}".format("_"*100))
        )