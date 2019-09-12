from ..jsonrpc.trx3 import *


def version():
    r = net_version()
    return r['result']


def peerCount():
    r = net_peerCount()
    number = int(r['result'], 16)
    return number


def listening():
    r = net_listening()
    return r['result']