import hashlib, time

class Block:
    def __init__(self, data, prev_hash=""):
        self.data = data
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.hash = self.calc_hash()

    def calc_hash(self):
        return hashlib.sha256((str(self.data) + self.prev_hash + str(self.timestamp)).encode()).hexdigest()

class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis()]

    def create_genesis(self):
        return Block("Genesis")

    def addBlock(self, block):
        block.prev_hash = self.chain[-1].hash
        block.hash = block.calc_hash()
        self.chain.append(block)

    def chainValid(self):
        for i in range(1, len(self.chain)):
            b, pb = self.chain[i], self.chain[i - 1]
            if b.hash != b.calc_hash() or b.prev_hash != pb.hash:
                return False
        return True
