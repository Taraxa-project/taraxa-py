from path import workspace
# from test.config import *

from pytaraxa import eth

eth.set({"host": "64.225.42.78"})

r = eth.blockNumber()
print(r)


boot_privateKey = "0x3800b2875669d9b2053c1aff9224ecfdc411423aac5b5a73d7a45ced1c3b9dcd"
boot_address = "0xde2b1203d72d3549EE2f733b00b2789414C7Cea5"

privateKey = "0x5076e3eae916b0c68b72a514a67fd089c643c2f306462bb64a99155bfb26757d"
address = "0x07162012099a6c3D44B264CD70aa9f390a26A0f3"

# '0xa16A181AD474C82D8753eB0C10e8DD4e5710314f'

r = eth.getBalance('0x07162012099a6c3D44B264CD70aa9f390a26A0f3')
print(r)

# r = eth.getBlockByNumber(0)
# print(r)

# r = eth.getTransactionByBlock(4, 0)
# print(r)
