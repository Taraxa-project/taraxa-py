# pytaraxa

Taraxa RPC client in python.  

pytaraxa pypi address: [pytaraxa](https://pypi.org/project/pytaraxa/)  

Taraxa official website: [taraxa.io](https://taraxa.io)  
## install
```
git clone https://github.com/Taraxa-project/taraxa-py
cd taraxa-py
python setup.py install
```
or
```
pip install pytaraxa
```
## config  

default parameters:  
``` python
config={
    "ip":"127.0.0.1",  
    "port":7777,  
    "jsonrpc":2.0,  
    "id":1
}
```
for all methods, if no parameter given, default will be used.

1. package level config set and reset.  
any of below config will influence the whole packge.
``` python
import pytaraxa.jsonrpc as rpc
import pytaraxa.eth as eth
import pytaraxa.taraxa as taraxa
import pytaraxaa.net as net

rpc.set({
    "ip":"127.0.0.1",  
    "port":7777,  
    "jsonrpc":2.0,  
    "id":1 
})

eth.set({
    "ip":"35.224.183.106",  
})
taraxa.set({
    "ip":"35.224.183.106",  
})
net.set({
    "ip":"35.224.183.106",  
})

rpc.reset()
eth.reset()
taraxa.reset()
net.reset()
```
2. function level config set  
function level config set only influence the function it self once.
``` python
import pytaraxa.eth as eth
r=eth.blockNumber(ip='127.0.0.1' ,port=7777)
print(r)
```

## usage





- low level use
``` python
import pytaraxa.jsonrpc as rpc
data = '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
r = rpc.send(data)
print(r)

data = {"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}
r = rpc.send(data)
print(r)
```
data can be json string or dict. response is json string.
- middle level use
``` python
from pytaraxa.jsonrpc  import *
r = eth_blockNumber()
print(r)
```
response is json string.
- high level use
``` python
import pytaraxa.eth as eth
r = eth.blockNumber()
print(r)
```
response is parsed to python types.
- ethereum web3 like use  

``` python
from pytaraxa.web3 import Web3
w3 = Web3(ip="35.224.183.106" ,port=7777)
r = w3.blockNumber()
print(r)

w3.ip = "35.224.183.106"
w3.port = 7778
r = w3.blockNumber()
print(r)
```
Web3 object w3 will hold the ip and port once you set.   
w3 method will use the ip and port you set until you reset it.
## sub packages
- jsonrpc  
- eth  
- web3  
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