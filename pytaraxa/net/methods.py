from ..jsonrpc.http_net import *


def version():
    r = net_version()
    return r['result']


def peerCount():
    r = net_peerCount()
    number = hex2int(r['result'])
    return number


def listening():
    r = net_listening()
    return r['result']