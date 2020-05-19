from .. import eth


def config(func):
    def wrap_func(*args, **kwargs):
        #print("config =====")
        # print(kwargs)
        return func(*args, **kwargs)
    return wrap_func


class ETH:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def set(self, **kwargs):
        host = kwargs.get("host", None)
        if host:
            self.host = host

        port = kwargs.get("port", None)
        if port:
            self.port = port

    @config
    def syncing(self, **kwargs):

        return eth.syncing(host=self.host, port=self.port, **kwargs)

    def coinbase(self, **kwargs):

        return eth.coinbase(host=self.host, port=self.port, **kwargs)

    def mining(self, **kwargs):

        return eth.mining(host=self.host, port=self.port, **kwargs)

    def hashrate(self, **kwargs):

        return eth.hashrate(host=self.host, port=self.port, **kwargs)

    def gasPrice(self, **kwargs):

        return eth.gasPrice(host=self.host, port=self.port, **kwargs)

    def accounts(self, **kwargs):

        return eth.accounts(host=self.host, port=self.port, **kwargs)

    def getBalance(self, address, tag="latest", **kwargs):

        return eth.getBalance(address, tag="latest", host=self.host,
                              port=self.port, **kwargs)

    @config
    def blockNumber(self, **kwargs):

        return eth.blockNumber(**kwargs)

    def getStorageAt(self, address, position, tag="latest", **kwargs):

        return eth.getStorageAt(address, position, tag="latest",
                                host=self.host, port=self.port, **kwargs)

    def getTransactionCount(self, address, tag="latest", **kwargs):

        return eth.getTransactionCount(address, tag="latest",
                                       host=self.host, port=self.port, **kwargs)

    def getBlockTransactionCountByHash(self, hash, **kwargs):

        return eth.getBlockTransactionCountByHash(
            hash, host=self.host, port=self.port, **kwargs)

    def getBlockTransactionCountByNumber(self, tag, **kwargs):

        return eth.getBlockTransactionCountByNumber(
            tag, host=self.host, port=self.port, **kwargs)

    def getUncleCountByBlockHash(self, hash, **kwargs):

        return eth.getUncleCountByBlockHash(
            hash, host=self.host, port=self.port, **kwargs)

    def getUncleCountByBlockNumber(self, tag, **kwargs):

        return eth.getUncleCountByBlockNumber(
            tag, host=self.host, port=self.port, **kwargs)

    def getCode(self, address, tag, **kwargs):

        return eth.getCode(address, tag, host=self.host, port=self.port, **kwargs)

    def sign(self, address, data, tag="latest", **kwargs):

        return eth.sign(address, data, tag="latest",
                        host=self.host, port=self.port, **kwargs)

    def sendTransaction(self, trx, **kwargs):

        return eth.sendTransaction(trx, host=self.host, port=self.port, **kwargs)

    def sendRawTransaction(self, trx, **kwargs):

        return eth.sendRawTransaction(trx, host=self.host, port=self.port, **kwargs)

    def call(self, trx, tag, **kwargs):

        return eth.call(trx, tag, host=self.host, port=self.port, **kwargs)

    def estimateGas(self, trx, tag, **kwargs):

        return eth.estimateGas(trx, tag, host=self.host, port=self.port, **kwargs)

    def getBlockByHash(self, hash, fullTransactions=False, **kwargs):

        return eth.getBlockByHash(hash, fullTransactions=False,
                                  host=self.host, port=self.port, **kwargs)

    def getBlockByNumber(self, tag, fullTransactions=False, **kwargs):

        return eth.getBlockByNumber(tag, fullTransactions=False,
                                    host=self.host, port=self.port, **kwargs)

    def getTransactionByHash(self, hash, **kwargs):

        return eth.getTransactionByHash(hash, host=self.host, port=self.port, **kwargs)

    def getTransactionByBlockHashAndIndex(self, hash, index, **kwargs):

        return eth.getTransactionByBlockHashAndIndex(
            hash, index, host=self.host, port=self.port, **kwargs)

    def getTransactionByBlockNumberAndIndex(self, tag, index, **kwargs):

        return eth.getTransactionByBlockNumberAndIndex(
            tag, index, host=self.host, port=self.port, **kwargs)

    def getTransactionReceipt(self, hash, **kwargs):

        return eth.getTransactionReceipt(hash, host=self.host, port=self.port, **kwargs)

    def pendingTransactions(self, **kwargs):

        return eth.pendingTransactions(host=self.host, port=self.port, **kwargs)

    def getUncleByBlockHashAndIndex(self, hash, index, **kwargs):

        return eth.getUncleByBlockHashAndIndex(
            hash, index, host=self.host, port=self.port, **kwargs)

    def getUncleByBlockNumberAndIndex(self, tag, index, **kwargs):

        return eth.getUncleByBlockNumberAndIndex(
            tag, index, host=self.host, port=self.port, **kwargs)

    def newFilter(self, filter, **kwargs):

        return eth.newFilter(filter, host=self.host, port=self.port, **kwargs)

    def newBlockFilter(self, **kwargs):

        return eth.newBlockFilter(host=self.host, port=self.port, **kwargs)

    def newPendingTransactionFilter(self, **kwargs):

        return eth.newPendingTransactionFilter(host=self.host, port=self.port, **kwargs)

    def uninstallFilter(self, id, **kwargs):

        return eth.uninstallFilter(id, host=self.host, port=self.port, **kwargs)
