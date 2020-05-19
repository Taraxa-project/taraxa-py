# taraxa-py

Taraxa RPC client in python.  

taraxa-py pypi address: [taraxa-py](https://pypi.org/project/taraxa-py/)  

Taraxa official website: [taraxa.io](https://taraxa.io)  
## install
install from source code.
```
git clone https://github.com/Taraxa-project/taraxa-py
cd taraxa-py
python setup.py install
```
or install from pypi [pytaraxa](https://pypi.org/project/pytaraxa/).  
```
pip install taraxa-py
```
## config  

default parameters:  
``` python
config={
    "host":"127.0.0.1",  
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
        "host":"127.0.0.1",  
        "port":7777,  
        "jsonrpc":2.0,  
        "id":1 
    })

    eth.set({
        "host":"35.224.183.106",  
    })
    taraxa.set({
        "host":"35.224.183.106",  
    })
    net.set({
        "host":"35.224.183.106",  
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
    r=eth.blockNumber(host='127.0.0.1' ,port=7777)
    print(r)
    ```

## usage

- 1.low level use  
    input data can be json string or dict.  
    response is json string.  
    ``` python
    import pytaraxa.jsonrpc as rpc
    data = '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
    r = rpc.send(data)
    print(r)

    data = {"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}
    r = rpc.send(data)
    print(r)
    ```


- 2.middle level use  
    response is json string.  
    ``` python
    from pytaraxa.jsonrpc  import *
    r = eth_blockNumber()
    print(r)
    ```


- 3.high level use  
    response is parsed to python types.  
    ``` python
    import pytaraxa.eth as eth
    r = eth.blockNumber()
    print(r)
    ```


- 4.ethereum [web3.py](https://github.com/ethereum/web3.py) like use  

    ``` python
    import pytaraxa import web3

    w3 = web3.Web3(host="127.0.0.0" ,port=7777)
    r = w3.eth.blockNumber()
    print(r)

    w3.host = "35.224.183.106"
    w3.port = 7778
    r = w3.eth.blockNumber()
    print(r)
    ```
    object w3 of class Web3  will hold the host and port once you set until you reset it to default.   

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