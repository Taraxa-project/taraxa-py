from ..jsonrpc.http_web3 import *


def clientVersion():
    r = web3_clientVersion()
    return r


def sha3(data):
    r = web3_sha3(data)
    return r['result']