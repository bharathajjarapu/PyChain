# PyChain
A Local Python BlockChain with Hashing

## Installation

Source code

```bash
git clone https://github.com/bharathajjarapu/PyChainn.git
```

## Usage

```python
from PyChain import BlockChain, Block

chain = BlockChain()
chain.addBlock(Block([1,2,3]))
chain.addBlock(Block([4,5,6]))
chain.addBlock(Block([7,8,9]))
chain.addBlock(Block([10,11,12]))

print(chain.chainValid())

for i in range(len(chain.chain)):
    print(i.data)
```
