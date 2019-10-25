from ..jsonrpc.http_taraxa import *


def dag_block_hex2int(block):
    keys = ['level', 'period', 'number', 'timestamp']
    for key in keys:
        block[key] = hex2int(block[key])
    return block


def getDagBlockByHash(hash, fullTransactions=False, **kwargs):
    r = taraxa_getDagBlockByHash(hash, fullTransactions, **kwargs)
    block = r['result']
    if 'result' in r:
        block = r['result']
        if block:
            block = dag_block_hex2int(block)
        return block
    else:
        raise Exception(r["error"])


def getDagBlockByLevel(tag, fullTransactions=False, **kwargs):
    r = taraxa_getDagBlockByLevel(tag, fullTransactions, **kwargs)
    if 'result' in r:
        blocks = r['result']
        blocks = list(map(lambda block: dag_block_hex2int(block), blocks))
        return blocks
    else:
        raise Exception(r["error"])


def dagBlockLevel(**kwargs):
    r = taraxa_dagBlockLevel(**kwargs)
    level = hex2int(r['result'])
    return level


def dagBlockPeriod(**kwargs):
    r = taraxa_dagBlockPeriod(**kwargs)
    period = hex2int(r['result'])
    return period


def blockNumber(**kwargs):
    r = taraxa_blockNumber(**kwargs)
    number = hex2int(r['result'])
    return number