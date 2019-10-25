from .utl import *
from ._http import *


@traxa_rpc
def taraxa_syncing():
    params = []
    return params


@traxa_rpc
def taraxa_coinbase(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_mining():
    params = []
    return params


@traxa_rpc
def taraxa_hashrate(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_gasPrice(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_accounts(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_getBalance(address, tag="latest", **kwargs):
    tag = tag_check(tag)
    params = [address, tag]
    return params


@traxa_rpc
def taraxa_blockNumber(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_getStorageAt(address, position, tag="latest", **kwargs):
    tag = tag_check(tag)
    params = [address, position, tag]
    return params


@traxa_rpc
def taraxa_getTransactionCount(address, tag="latest", **kwargs):
    tag = tag_check(tag)
    params = [address, tag]
    return params


@traxa_rpc
def taraxa_getBlockTransactionCountByHash(hash, **kwargs):
    params = [hash]
    return params


@traxa_rpc
def taraxa_getBlockTransactionCountByNumber(tag, **kwargs):
    tag = tag_check(tag)
    params = [tag]
    return params


@traxa_rpc
def taraxa_getUncleCountByBlockHash(hash, **kwargs):
    params = [hash]
    return params


@traxa_rpc
def taraxa_getUncleCountByBlockNumber(tag, **kwargs):
    tag = tag_check(tag)
    params = [tag]
    return params


@traxa_rpc
def taraxa_getCode(address, tag, **kwargs):
    tag = tag_check(tag)
    params = [address, tag]
    return params


# TODO
@traxa_rpc
def taraxa_sign(address, data, tag="latest", **kwargs):
    tag = tag_check(tag)
    params = [address, data]
    return params


# TODO
@traxa_rpc
def taraxa_sendTransaction(trx, **kwargs):
    params = [trx]
    return params


@traxa_rpc
def taraxa_sendRawTransaction(trx, tag="latest", **kwargs):
    tag = tag_check(tag)
    params = [trx]
    return params


# TODO
@traxa_rpc
def taraxa_call(trx, tag, **kwargs):
    tag = tag_check(tag)
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
def taraxa_estimateGas(trx, tag, **kwargs):
    tag = tag_check(tag)
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
def taraxa_getBlockByHash(hash, fullTransactions=False, **kwargs):
    params = [hash, fullTransactions]
    return params


@traxa_rpc
def taraxa_getBlockByNumber(tag, fullTransactions=False, **kwargs):
    tag = tag_check(tag)
    params = [tag, fullTransactions]
    return params


@traxa_rpc
def taraxa_getTransactionByHash(hash, **kwargs):
    params = [hash]
    return params


@traxa_rpc
def taraxa_getTransactionByBlockHashAndIndex(hash, index, **kwargs):
    params = [hash, index]
    return params


@traxa_rpc
def taraxa_getTransactionByBlockNumberAndIndex(tag, index, **kwargs):
    tag = tag_check(tag)
    params = [tag, index]
    return params


@traxa_rpc
def taraxa_getTransactionReceipt(hash, **kwargs):
    params = [hash]
    return params


@traxa_rpc
def taraxa_pendingTransactions(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_getUncleByBlockHashAndIndex(hash, index, **kwargs):
    params = [hash, index]
    return params


@traxa_rpc
def taraxa_getUncleByBlockNumberAndIndex(tag, index, **kwargs):
    tag = tag_check(tag)
    params = [tag, index]
    return params


@traxa_rpc
def taraxa_newFilter(filter, **kwargs):
    params = [filter]
    return params


@traxa_rpc
def taraxa_newBlockFilter(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_newPendingTransactionFilter(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_uninstallFilter(id, **kwargs):
    params = [id]
    return params


@traxa_rpc
def taraxa_getFilterChanges(id, **kwargs):
    params = [id]
    return params


@traxa_rpc
def taraxa_getFilterLogs(id, **kwargs):
    params = [id]
    return params


@traxa_rpc
def taraxa_getLogs(filter, **kwargs):
    params = [filter]
    return params


@traxa_rpc
def taraxa_getWork(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_submitWork(nonce, header_power_hash, mix_digest, **kwargs):
    params = [nonce, header_power_hash, mix_digest]
    return params


@traxa_rpc
def taraxa_submitHashrate(hash_rate, id, **kwargs):
    params = [hash_rate, id]
    return params


@traxa_rpc
def taraxa_getProof(address, storage_keys, tag, **kwargs):
    tag = tag_check(tag)
    params = [address, storage_keys, tag]
    return params


#=============
#below is only taraxa rpc, not in eth
#=============


@traxa_rpc
def taraxa_getStorageRoot(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_flush(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_newFilterEx(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_getFilterChangesEx(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_getFilterLogsEx(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_getLogsEx(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_register(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_unregister(**kwargs):
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


@traxa_rpc
def taraxa_signTransaction(address, data, tag="latest", **kwargs):
    tag = tag_check(tag)
    params = [address, data]
    return params


@traxa_rpc
def taraxa_getDagBlockByHash(hash, fullTransactions=False, **kwargs):
    params = [hash, fullTransactions]
    return params


@traxa_rpc
def taraxa_getDagBlockByLevel(tag, fullTransactions=False, **kwargs):
    tag = tag_check(tag)
    params = [tag, fullTransactions]
    return params


@traxa_rpc
def taraxa_dagBlockLevel(**kwargs):
    params = []
    return params


@traxa_rpc
def taraxa_dagBlockPeriod(**kwargs):
    params = []
    return params