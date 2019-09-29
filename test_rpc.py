import pytaraxa.jsonrpc as rpc


#=============
def getDagBlockByHash():
    hash = "0x926b67dd4f7a3b838707f03fda7a9d78a14f9b26040d231c76164f62908750d1"
    data = {"jsonrpc": "2.0", "method": "taraxa_getDagBlockHash", "params": [hash], "id": 1}
    r = rpc.send(data, ip='127.0.0.1', port=7777)
    print(r.json())


def getDagBlockByLevel():
    tag = 2
    tag = rpc.tag_check(tag)
    data = {"jsonrpc": "2.0", "method": "taraxa_dagBlockLevel", "params": [], "id": 1}
    r = rpc.send(data, ip='127.0.0.1', port=7777)
    print(r.json())


if __name__ == "__main__":
    getDagBlockByHash()