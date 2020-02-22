from .. import eth


class Web3:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def syncing(self, **kwargs):

        eth.syncing(ip=self.ip, port=self.port, **kwargs)

    def coinbase(self, **kwargs):

        eth.coinbase(ip=self.ip, port=self.port, **kwargs)

    def mining(self, **kwargs):

        eth.mining(ip=self.ip, port=self.port, **kwargs)

    def hashrate(self, **kwargs):

        eth.hashrate(ip=self.ip, port=self.port, **kwargs)

    def gasPrice(self, **kwargs):

        eth.gasPrice(ip=self.ip, port=self.port, **kwargs)

    def accounts(self, **kwargs):

        eth.accounts(ip=self.ip, port=self.port, **kwargs)

    def getBalance(self, address, tag="latest", **kwargs):

        eth.getBalance(address, tag="latest", ip=self.ip, port=self.port, **kwargs)

    def blockNumber(self, **kwargs):

        eth.blockNumber(ip=self.ip, port=self.port, **kwargs)

    def getStorageAt(self, address, position, tag="latest", **kwargs):

        eth.getStorageAt(address, position, tag="latest", ip=self.ip, port=self.port, **kwargs)

    def getTransactionCount(self, address, tag="latest", **kwargs):

        eth.getTransactionCount(address, tag="latest", ip=self.ip, port=self.port, **kwargs)

    def getBlockTransactionCountByHash(self, hash, **kwargs):

        eth.getBlockTransactionCountByHash(hash, ip=self.ip, port=self.port, **kwargs)

    def getBlockTransactionCountByNumber(self, tag, **kwargs):

        eth.getBlockTransactionCountByNumber(tag, ip=self.ip, port=self.port, **kwargs)

    def getUncleCountByBlockHash(self, hash, **kwargs):

        eth.getUncleCountByBlockHash(hash, ip=self.ip, port=self.port, **kwargs)

    def getUncleCountByBlockNumber(self, tag, **kwargs):

        eth.getUncleCountByBlockNumber(tag, ip=self.ip, port=self.port, **kwargs)

    def getCode(self, address, tag, **kwargs):

        eth.getCode(address, tag, ip=self.ip, port=self.port, **kwargs)

    def sign(self, address, data, tag="latest", **kwargs):

        eth.sign(address, data, tag="latest", ip=self.ip, port=self.port, **kwargs)

    def sendTransaction(self, trx, **kwargs):

        eth.sendTransaction(trx, ip=self.ip, port=self.port, **kwargs)

    def sendRawTransaction(self, trx, **kwargs):

        eth.sendRawTransaction(trx, ip=self.ip, port=self.port, **kwargs)

    def call(self, trx, tag, **kwargs):

        eth.call(trx, tag, ip=self.ip, port=self.port, **kwargs)

    def estimateGas(self, trx, tag, **kwargs):

        eth.estimateGas(trx, tag, ip=self.ip, port=self.port, **kwargs)

    def getBlockByHash(self, hash, fullTransactions=False, **kwargs):

        eth.getBlockByHash(hash, fullTransactions=False, ip=self.ip, port=self.port, **kwargs)

    def getBlockByNumber(self, tag, fullTransactions=False, **kwargs):

        eth.getBlockByNumber(tag, fullTransactions=False, ip=self.ip, port=self.port, **kwargs)

    def getTransactionByHash(self, hash, **kwargs):

        eth.getTransactionByHash(hash, ip=self.ip, port=self.port, **kwargs)

    def getTransactionByBlockHashAndIndex(self, hash, index, **kwargs):

        eth.getTransactionByBlockHashAndIndex(hash, index, ip=self.ip, port=self.port, **kwargs)

    def getTransactionByBlockNumberAndIndex(self, tag, index, **kwargs):

        eth.getTransactionByBlockNumberAndIndex(tag, index, ip=self.ip, port=self.port, **kwargs)

    def getTransactionReceipt(self, hash, **kwargs):

        eth.getTransactionReceipt(hash, ip=self.ip, port=self.port, **kwargs)

    def pendingTransactions(self, **kwargs):

        eth.pendingTransactions(ip=self.ip, port=self.port, **kwargs)

    def getUncleByBlockHashAndIndex(self, hash, index, **kwargs):

        eth.getUncleByBlockHashAndIndex(hash, index, ip=self.ip, port=self.port, **kwargs)

    def getUncleByBlockNumberAndIndex(self, tag, index, **kwargs):

        eth.getUncleByBlockNumberAndIndex(tag, index, ip=self.ip, port=self.port, **kwargs)

    def newFilter(self, filter, **kwargs):

        eth.newFilter(filter, ip=self.ip, port=self.port, **kwargs)

    def newBlockFilter(self, **kwargs):

        eth.newBlockFilter(ip=self.ip, port=self.port, **kwargs)

    def newPendingTransactionFilter(self, **kwargs):

        eth.newPendingTransactionFilter(ip=self.ip, port=self.port, **kwargs)

    def uninstallFilter(self, id, **kwargs):

        eth.uninstallFilter(id, ip=self.ip, port=self.port, **kwargs)
