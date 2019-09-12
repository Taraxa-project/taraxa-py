# pytaraxa

taraxa python rpc client
## install
```
python setup.py install
```
## usage

default parameters:  
```
ip:127.0.0.1  
port:7777  
jsonrpc:2.0  
id:1  
```
for all methods, if no parameter given, default will be used.
- low level use
``` python
import pytaraxa.jsonrpc as rpc
data='{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
r=rpc.send(data,ip='127.0.0.1' ,port=7777)
print(r)

data={"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}
r=rpc.send(data,ip='127.0.0.1' ,port=7777)
print(r)
```
data can be json string or dict. response is json string.
- middle level use
``` python
from pytaraxa.jsonrpc  import *
r=eth_blockNumber(ip='127.0.0.1' ,port=7777)
print(r)
```
response is json string.
- high level use
``` python
import pytaraxa.eth as eth
r=eth.blockNumber(ip='127.0.0.1' ,port=7777)
print(r)
```
response is parsed to python types.
- ethereum web3 like use  

``` python
from pytaraxa.web3 import Web3
w3=Web3(ip='127.0.0.1' ,port=7777)
r=w3.blockNumber()
print(r)

w3.ip= 'x.x.x.x'
w3.port= 7778
r=w3.blockNumber()
print(r)
```
Web3 object w3 will hold the ip and port once you set.   
w3 method will use the ip and port you set until you reset it.
## sub packages
- jsonrpc  
- eth  
- web3  
TODO
- net  
TODO
- admin  
TODO
- admmin_net  
TODO
- debug  
TODO
- test  
TODO