from path import workspace
from pytaraxa.jsonrpc.http_eth import *
address = [
    "de2b1203d72d3549ee2f733b00b2789414c7cea5", "973ecb1c08c8eb5a7eaa0d3fd3aab7924f2838b0",
    "4fae949ac2b72960fbe857b56532e2d3c8418d5e", "415cf514eb6a5a8bd4d325d4874eae8cf26bcfe0",
    "b770f7a99d0b7ad9adf6520be77ca20ee99b0858"
]
# r = eth_getBlockByHash('0x1571a0204e280d854d1c26821f4a77936745a9d9b869fcf7f18d3f6db74d42ce',
#                        True)
# print(r['result'])
#trx = {'a': 1}
#r = eth_sendTransaction(trx, host='333.333')
tags = ["latest", '10', '0xa', 10, 0xa]
for t in tags:
    print(tag_check(t))
