from ..jsonrpc.http_web3 import *
from .eth import ETH


class Web3:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.eth = ETH(self.host, self.port)

    def __setattr__(self, name, value):
        # if name == 'host':
        #     # print(name)
        #     # print(value)
        return super().__setattr__(name, value)

    def clientVersion(self):
        r = web3_clientVersion()
        return r

    def sha3(self, data):
        r = web3_sha3(data)
        return r['result']
