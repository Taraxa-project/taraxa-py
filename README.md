# pytaraxa

taraxa python rpc client
## install
```
python setup.py install
```
## usage

default ip:127.0.0.1  
default port:7777  

- low level use
```
import pytaraxa.jsonrpc as rpc
data='{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
r=rpc.send(data,ip='127.0.0.1' ,port=7777)
print(r)
```
- middle level use
```
from pytaraxa.jsonrpc  import *
r=eth_blockNumber(ip='127.0.0.1' ,port=7777)
print(r)
```
- high level use
```
import pytaraxa.eth as eth
r=eth.blockNumber(ip='127.0.0.1' ,port=7777)
print(r)
```
- ethereum web3 like use
```
from pytaraxa.web3 import Web3
w3=Web3(ip='127.0.0.1' ,port=7777)
r=w3.blockNumber()
print(r)
```
## sub packages
- jsonrpc
- eth
- web3
- net
- admin
- admmin_net
- debug
- test