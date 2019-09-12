import requests
import json

Node_ip = "0.0.0.0"
Node_port = 7777


def send(data, node_ip=Node_ip, node_port=Node_port):
    if type(data) == dict:
        data = json.dumps(data)
    elif type(data) == str:
        pass
    else:
        print('send data must be json string or dict')
        return None

    try:
        request = requests.post("http://{}:{}".format(node_ip, node_port), data=data)
    except Exception as e:
        print(e)
        request = None
    return request


def message(jsonrpc, method, params, id):
    trx = {"jsonrpc": jsonrpc, "method": method, "params": params, "id": id}
    return json.dumps(trx)


def traxa_rpc(func):

    def wrap_func(*args, **kwargs):
        #要提交的参数
        jsonrpc = kwargs.get("jsonrpc", "2.0")  #默认参数
        method = func.__name__  #jsonrpc方法名同函数名
        params = func(*args, **kwargs)
        id = kwargs.get("id", 1)  #默认参数
        msg = message(jsonrpc, method, params, id)

        #要提交的节点
        ip = kwargs.get("ip", Node_ip)
        port = kwargs.get("port", Node_port)
        r = send(msg, ip, port)

        return r.json()

    return wrap_func


# TODO
@traxa_rpc
def web3_clientVersion(**kwargs):
    params = []
    return params


# TODO
@traxa_rpc
def web3_sha3(data, **kwargs):
    params = [data]
    return params


@traxa_rpc
def net_version(**kwargs):
    params = []
    return params


@traxa_rpc
def net_peerCount(**kwargs):
    params = []
    return params


@traxa_rpc
def net_listening(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_syncing():
    params = []
    return params


@traxa_rpc
def eth_coinbase(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_mining():
    params = []
    return params


@traxa_rpc
def eth_hashrate(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_gasPrice(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_accounts(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_getBalance(address, tag="latest", **kwargs):
    params = [address, tag]
    return params


@traxa_rpc
def eth_blockNumber(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_getStorageAt(address, position, tag="latest", **kwargs):
    params = [address, position, tag]
    return params


@traxa_rpc
def eth_getTransactionCount(address, tag="latest", **kwargs):
    params = [address, tag]
    return params


@traxa_rpc
def eth_getBlockTransactionCountByHash(hash, **kwargs):
    params = [hash]
    return params


@traxa_rpc
def eth_getBlockTransactionCountByNumber(tag, **kwargs):
    params = [tag]
    return params


@traxa_rpc
def eth_getUncleCountByBlockHash(hash, **kwargs):
    params = [hash]
    return params


@traxa_rpc
def eth_getUncleCountByBlockNumber(tag, **kwargs):
    params = [tag]
    return params


@traxa_rpc
def eth_getCode(address, tag, **kwargs):
    params = [address, tag]
    return params


# TODO
@traxa_rpc
def eth_sign(address, data, tag="latest", **kwargs):
    params = [address, data]
    return params


# TODO
@traxa_rpc
def eth_sendTransaction(trx, **kwargs):
    params = [trx]
    return params


@traxa_rpc
def eth_sendRawTransaction(trx, tag="latest", **kwargs):
    params = [trx]
    return params


# TODO
@traxa_rpc
def eth_call(trx, tag, **kwargs):
    params = [
        {
            # "from": trx['from'],
            # "to": trx['to'],
            # "gas": trx['gas'],
            # "gasPrice": trx['gasPrice'],
            # "value": trx['value'],
            # "data": trx['data'],
        },
        tag
    ]
    return params


# TODO
@traxa_rpc
def eth_estimateGas(trx, tag, **kwargs):
    params = [
        {
            # "from": trx['from'],
            # "to": trx['to'],
            # "gas": trx['gas'],
            # "gasPrice": trx['gasPrice'],
            # "value": trx['value'],
            # "data": trx['data'],
        },
        tag
    ]
    return params


@traxa_rpc
def eth_getBlockByHash(hash, fullTransactions=False, **kwargs):
    params = [hash, fullTransactions]
    return params


@traxa_rpc
def eth_getBlockByNumber(tag, fullTransactions=False, **kwargs):
    params = [tag, fullTransactions]
    return params


@traxa_rpc
def eth_getTransactionByHash(hash, **kwargs):
    params = [hash]
    return params


@traxa_rpc
def eth_getTransactionByBlockHashAndIndex(hash, index, **kwargs):
    params = [hash, index]
    return params


@traxa_rpc
def eth_getTransactionByBlockNumberAndIndex(tag, index, **kwargs):
    params = [tag, index]
    return params


@traxa_rpc
def eth_getTransactionReceipt(hash, **kwargs):
    params = [hash]
    return params


@traxa_rpc
def eth_pendingTransactions(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_getUncleByBlockHashAndIndex(hash, index, **kwargs):
    params = [hash, index]
    return params


@traxa_rpc
def eth_getUncleByBlockNumberAndIndex(tag, index, **kwargs):
    params = [tag, index]
    return params


@traxa_rpc
def eth_newFilter(filter, **kwargs):
    params = [filter]
    return params


@traxa_rpc
def eth_newBlockFilter(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_newPendingTransactionFilter(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_uninstallFilter(id, **kwargs):
    params = [id]
    return params


@traxa_rpc
def eth_getFilterChanges(id, **kwargs):
    params = [id]
    return params


@traxa_rpc
def eth_getFilterLogs(id, **kwargs):
    params = [id]
    return params


@traxa_rpc
def eth_getLogs(filter, **kwargs):
    params = [filter]
    return params


@traxa_rpc
def eth_getWork(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_submitWork(nonce, header_power_hash, mix_digest, **kwargs):
    params = [nonce, header_power_hash, mix_digest]
    return params


@traxa_rpc
def eth_submitHashrate(hash_rate, id, **kwargs):
    params = [hash_rate, id]
    return params


@traxa_rpc
def eth_getProof(address, storage_keys, tag, **kwargs):
    params = [address, storage_keys, tag]
    return params


#=============
#below is only taraxa rpc, not in eth
#=============


@traxa_rpc
def eth_getStorageRoot(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_flush(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_newFilterEx(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_getFilterChangesEx(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_getFilterLogsEx(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_getLogsEx(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_register(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_unregister(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_fetchQueuedTransactions(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_signTransaction(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_inspectTransaction(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_notePassword(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_chainId(**kwargs):
    params = []
    return params


def taraxa_getDagBlockByHash(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_getDagBlockByLevel(**kwargs):
    params = []
    return params


@traxa_rpc
def eth_signTransaction(address, data, tag="latest", **kwargs):
    params = [address, data]
    return params


if __name__ == "__main__":
    address = [
        "de2b1203d72d3549ee2f733b00b2789414c7cea5", "973ecb1c08c8eb5a7eaa0d3fd3aab7924f2838b0",
        "4fae949ac2b72960fbe857b56532e2d3c8418d5e", "415cf514eb6a5a8bd4d325d4874eae8cf26bcfe0",
        "b770f7a99d0b7ad9adf6520be77ca20ee99b0858"
    ]
    # r = eth_getBlockByHash('0x1571a0204e280d854d1c26821f4a77936745a9d9b869fcf7f18d3f6db74d42ce',
    #                        True)
    # print(r['result'])
    trx = {'a': 1}
    r = eth_sendTransaction(trx, ip='333.333')
