from ..jsonrpc.http_taraxa import *


def getDagBlockByHash(hash, fullTransactions=False, **kwargs):
    r = taraxa_getDagBlockByHash(hash, fullTransactions, **kwargs)
    print(r)
    block = r['result']
    return block


def getDagBlockByLevel(tag, fullTransactions=False, **kwargs):
    r = taraxa_getDagBlockByLevel(tag, fullTransactions, **kwargs)
    print(r)
    block = r['result']
    return block


def dagBlockLevel(**kwargs):
    r = taraxa_dagBlockLevel(**kwargs)
    level = int(r['result'], 16)
    return level


def dagBlockPeriod(**kwargs):
    r = taraxa_dagBlockPeriod(**kwargs)
    period = int(r['result'], 16)
    return period


def blockNumber(**kwargs):
    r = taraxa_blockNumber(**kwargs)
    number = int(r['result'], 16)
    return number