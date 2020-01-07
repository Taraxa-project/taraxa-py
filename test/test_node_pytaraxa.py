from path import workspace
from test.config import *

from pytaraxa import eth

eth.set({"ip": "64.225.42.78"})

r = eth.blockNumber()
print(r)
r = eth.getBlockByNumber(0)
print(r)


# r = eth.getTransactionByBlock(4, 0)
# print(r)
