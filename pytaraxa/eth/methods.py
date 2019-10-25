from ..jsonrpc.http_eth import *


def syncing(**kwargs):
    r = eth_syncing(**kwargs)
    return r['result']


def coinbase(**kwargs):
    r = eth_coinbase(**kwargs)
    return r['result']


def mining(**kwargs):
    r = eth_mining(**kwargs)
    return r['result']


def hashrate(**kwargs):
    r = eth_hashrate(**kwargs)
    number = hex2int(r['result'])
    return number


#TODO
def gasPrice(**kwargs):
    r = eth_gasPrice(**kwargs)
    return r


def accounts(**kwargs):
    r = eth_accounts(**kwargs)
    return r['result']


def getBalance(address, tag="latest", **kwargs):
    r = eth_getBalance(address, tag)
    number = hex2int(r['result'])
    return number


def blockNumber(**kwargs):
    r = eth_blockNumber(**kwargs)
    number = hex2int(r['result'])
    return number


#no in taraxa rpc
def getStorageAt(address, position, tag="latest", **kwargs):
    r = eth_getStorageAt(**kwargs)
    return r


#no in taraxa rpc
def getTransactionCount(address, tag="latest", **kwargs):
    r = eth_getTransactionCount(address, tag, **kwargs)
    number = hex2int(r['result'])
    return number


#no in taraxa rpc
def getBlockTransactionCountByHash(hash, **kwargs):
    r = eth_getTransactionCount(hash, **kwargs)
    number = hex2int(r['result'])
    return number


def getBlockTransactionCountByNumber(tag="latest", **kwargs):
    r = eth_getBlockTransactionCountByNumber(tag, **kwargs)
    return r['result']


def getUncleCountByBlockHash(hash, **kwargs):
    r = eth_getUncleCountByBlockHash(hash, **kwargs)
    return r['result']


def getUncleCountByBlockNumber(tag="latest", **kwargs):
    r = eth_getUncleCountByBlockNumber(tag, **kwargs)
    return r['result']


def getCode(address, tag="latest", **kwargs):
    r = eth_getCode(address, tag, **kwargs)
    return r['result']


def sign(address, data, tag="latest", **kwargs):
    r = eth_sign(address, data, tag, **kwargs)
    return r['result']


def sendTransaction(trx, **kwargs):
    r = eth_sendTransaction(trx, **kwargs)
    return r['result']


def sendRawTransaction(trx, **kwargs):
    r = eth_sendRawTransaction(trx, **kwargs)
    return r['result']


def call(trx, tag="latest", **kwargs):
    r = eth_call(trx, **kwargs)
    return r


def estimateGas(trx, tag="latest", **kwargs):
    r = eth_estimateGas(trx, tag, **kwargs)
    return r


def getBlockByHash(hash, fullTransactions=False, **kwargs):
    r = eth_getBlockByHash(hash, fullTransactions, **kwargs)
    block = r['result']
    if not block:
        return block
    block_key_number = [
        'difficulty', 'gasUsed', 'nonce', 'number', 'size', 'timestamp', 'totalDifficulty'
    ]
    for key in block_key_number:
        block[key] = hex2int(block[key])
    return block


def getBlockByNumber(tag, fullTransactions=False, **kwargs):
    r = eth_getBlockByNumber(tag, fullTransactions, **kwargs)
    block = r['result']
    if not block:
        return block
    block_key_number = [
        'difficulty', 'gasUsed', 'nonce', 'number', 'size', 'timestamp', 'totalDifficulty'
    ]
    for key in block_key_number:
        block[key] = hex2int(block[key])
    return block


def getTransactionByHash(hash, **kwargs):
    r = eth_getTransactionByHash(hash, **kwargs)
    return r


def getTransactionByBlockHashAndIndex(hash, index, **kwargs):
    r = eth_getTransactionByBlockHashAndIndex(hash, index, **kwargs)
    return r


def getTransactionByBlockNumberAndIndex(tag, index, **kwargs):
    r = eth_getTransactionByBlockNumberAndIndex(tag, index, **kwargs)
    return r


def getTransactionReceipt(hash, **kwargs):
    r = eth_getTransactionReceipt(hash)
    return r


def pendingTransactions(**kwargs):
    r = eth_pendingTransactions(**kwargs)
    return r['result']


def getUncleByBlockHashAndIndex(hash, index, **kwargs):
    r = eth_getUncleByBlockHashAndIndex(hash, index, **kwargs)
    return r['result']


def getUncleByBlockNumberAndIndex(tag, index, **kwargs):
    r = eth_getUncleByBlockNumberAndIndex(tag, index, **kwargs)
    return r['result']


def newFilter(filter, **kwargs):
    r = eth_newFilter(filter, **kwargs)
    return r['result']


def newBlockFilter(**kwargs):
    r = eth_newBlockFilter(**kwargs)
    return r['result']


def newPendingTransactionFilter(**kwargs):
    r = eth_newPendingTransactionFilter(**kwargs)
    return r['result']


def uninstallFilter(id, **kwargs):
    r = eth_uninstallFilter(id, **kwargs)
    return r['result']


def getFilterChanges(id, **kwargs):
    r = eth_getFilterChanges(id, **kwargs)
    return r['result']


def getFilterLogs(id, **kwargs):
    r = eth_getFilterLogs(id, **kwargs)
    return r['result']


def getLogs(filter, **kwargs):
    r = eth_getLogs(filter, **kwargs)
    return r['result']


def getWork(**kwargs):
    r = eth_getWork(**kwargs)
    return r['result']


def submitWork(nonce, header_power_hash, mix_digest, **kwargs):
    r = eth_submitWork(nonce, header_power_hash, mix_digest, **kwargs)
    return r['result']


def submitHashrate(hash_rate, id, **kwargs):
    r = eth_submitHashrate(hash_rate, id, **kwargs)
    return r['result']


def getProof(address, storage_keys, tag, **kwargs):
    r = eth_getProof(address, storage_keys, tag, **kwargs)
    return r['result']


if __name__ == "__main__":
    blockNumber()
