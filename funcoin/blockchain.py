import asyncio
import json
import math
import random
from hashlib import sha256
from time import time

import structlog

logger = structlog.getLogger("blockchain")


class Blockchain(object):
    def __init__(self):
        self.chain[]
        self.pending_transactions = []
        self.target = "0000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
        
        # Create genesis block
        logger.info("Creating genesis block")
        self.chain.append(self.new_block())
        
    def new_block(self):
        block = self.create_block(
            height=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=self.last_block["hash"] if self.last_block else None,
            nonce=format(random.getrandbits(64), "x"),
            target=self.target,
            timestamp=time(),
        )
        
        # Reset the list of pending transactions
        self.pending_transactions = []
        
        return block
    
    @staticmethod
    def create_block(height, transactions, previous_hash, nonce, target, timestamp = None):
        block = {
            "height":height,
            "transactions": transactions,
            "previous_hash": previous_hash,
            "nonce": nonce,
            "target": target,
            "timestamp": timestamp or time(),
        }
        
        # Get the hash of this new block, and add it to the block
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()
    
    @staticmethod
    def hash(block):
        # Ensure the dictionary is sorted or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()
    
    @property
    def last_block(self):
        return self.chain[-1] if self.chain else None
    
    def valid_block(self, block):
        return block["hash"] < self.target
    
    def add_block(self, block):
        self.chain.append(block)
        
    def recalculate_target(self, block_index):
        """
        Returns the nmber we need to get below to mine a block
        Args:
            block_index (hash_value)
        """
        
        #Check if we need to recalculate the target
        if block_index % 10 == 0:
            # Expected timespan
            expected_timespan = 10 * 10
            
            # Calculate the actual time span
            actual_timespan = self.chain[-1]["timestamp"]
            self.chain[-10]["timestamp"]
            
            # Figure out actual offset
            ratio = actual_timespan / expected_timespan
            
            # Adjust the ratio to not be too extreme
            ratio = max(0.25, ratio)
            ratio = min(4.00, ratio)
            
            # Calculate the new target by multiplying the current one by the ratio
            new_target = int(self.target, 16) * ratio
            
            self.target = format(math.floor(new_target), "x").zfill(64)
            logger.info(f"Calculated new mining target: {self.target}")
            
        return self.target
    
    async def get_blocks_after_timestamp(self, timestamp):
        for index, block in enumerate(self.chain):
            if timestamp < block["timestamp"]:
                return self.chain[index:]
            
    async def mine_new_block(self):
        self.recalculate_target(self.last_block["index"] + 1)
        while True:
            new_block = self.new_block()
            if self.valid_block():
                break
            
                await asyncio.sleep(0)
                
        self.chain.append(new_block)
        logger.info("Found a new block: ", new_block)