from .. import eth


class Web3:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def syncing(self, **kwargs):

        return eth.syncing(ip=self.ip, port=self.port, **kwargs)

    def coinbase(self, **kwargs):

        return eth.coinbase(ip=self.ip, port=self.port, **kwargs)

    def mining(self, **kwargs):

        return eth.mining(ip=self.ip, port=self.port, **kwargs)

    def hashrate(self, **kwargs):

        return eth.hashrate(ip=self.ip, port=self.port, **kwargs)

    def gasPrice(self, **kwargs):

        return eth.gasPrice(ip=self.ip, port=self.port, **kwargs)

    def accounts(self, **kwargs):

        return eth.accounts(ip=self.ip, port=self.port, **kwargs)

    def getBalance(self, address, tag="latest", **kwargs):

        return eth.getBalance(address, tag="latest", ip=self.ip,
                              port=self.port, **kwargs)

    def blockNumber(self, **kwargs):

        return eth.blockNumber(ip=self.ip, port=self.port, **kwargs)

    def getStorageAt(self, address, position, tag="latest", **kwargs):

        return eth.getStorageAt(address, position, tag="latest",
                                ip=self.ip, port=self.port, **kwargs)

    def getTransactionCount(self, address, tag="latest", **kwargs):

        return eth.getTransactionCount(address, tag="latest",
                                       ip=self.ip, port=self.port, **kwargs)

    def getBlockTransactionCountByHash(self, hash, **kwargs):

        return eth.getBlockTransactionCountByHash(
            hash, ip=self.ip, port=self.port, **kwargs)

    def getBlockTransactionCountByNumber(self, tag, **kwargs):

        return eth.getBlockTransactionCountByNumber(
            tag, ip=self.ip, port=self.port, **kwargs)

    def getUncleCountByBlockHash(self, hash, **kwargs):

        return eth.getUncleCountByBlockHash(
            hash, ip=self.ip, port=self.port, **kwargs)

    def getUncleCountByBlockNumber(self, tag, **kwargs):

        return eth.getUncleCountByBlockNumber(
            tag, ip=self.ip, port=self.port, **kwargs)

    def getCode(self, address, tag, **kwargs):

        return eth.getCode(address, tag, ip=self.ip, port=self.port, **kwargs)

    def sign(self, address, data, tag="latest", **kwargs):

        return eth.sign(address, data, tag="latest",
                        ip=self.ip, port=self.port, **kwargs)

    def sendTransaction(self, trx, **kwargs):

        return eth.sendTransaction(trx, ip=self.ip, port=self.port, **kwargs)

    def sendRawTransaction(self, trx, **kwargs):

        return eth.sendRawTransaction(trx, ip=self.ip, port=self.port, **kwargs)

    def call(self, trx, tag, **kwargs):

        return eth.call(trx, tag, ip=self.ip, port=self.port, **kwargs)

    def estimateGas(self, trx, tag, **kwargs):

        return eth.estimateGas(trx, tag, ip=self.ip, port=self.port, **kwargs)

    def getBlockByHash(self, hash, fullTransactions=False, **kwargs):

        return eth.getBlockByHash(hash, fullTransactions=False,
                                  ip=self.ip, port=self.port, **kwargs)

    def getBlockByNumber(self, tag, fullTransactions=False, **kwargs):

        return eth.getBlockByNumber(tag, fullTransactions=False,
                                    ip=self.ip, port=self.port, **kwargs)

    def getTransactionByHash(self, hash, **kwargs):

        return eth.getTransactionByHash(hash, ip=self.ip, port=self.port, **kwargs)

    def getTransactionByBlockHashAndIndex(self, hash, index, **kwargs):

        return eth.getTransactionByBlockHashAndIndex(
            hash, index, ip=self.ip, port=self.port, **kwargs)

    def getTransactionByBlockNumberAndIndex(self, tag, index, **kwargs):

        return eth.getTransactionByBlockNumberAndIndex(
            tag, index, ip=self.ip, port=self.port, **kwargs)

    def getTransactionReceipt(self, hash, **kwargs):

        return eth.getTransactionReceipt(hash, ip=self.ip, port=self.port, **kwargs)

    def pendingTransactions(self, **kwargs):

        return eth.pendingTransactions(ip=self.ip, port=self.port, **kwargs)

    def getUncleByBlockHashAndIndex(self, hash, index, **kwargs):

        return eth.getUncleByBlockHashAndIndex(
            hash, index, ip=self.ip, port=self.port, **kwargs)

    def getUncleByBlockNumberAndIndex(self, tag, index, **kwargs):

        return eth.getUncleByBlockNumberAndIndex(
            tag, index, ip=self.ip, port=self.port, **kwargs)

    def newFilter(self, filter, **kwargs):

        return eth.newFilter(filter, ip=self.ip, port=self.port, **kwargs)

    def newBlockFilter(self, **kwargs):

        return eth.newBlockFilter(ip=self.ip, port=self.port, **kwargs)

    def newPendingTransactionFilter(self, **kwargs):

        return eth.newPendingTransactionFilter(ip=self.ip, port=self.port, **kwargs)

    def uninstallFilter(self, id, **kwargs):

        return eth.uninstallFilter(id, ip=self.ip, port=self.port, **kwargs)
