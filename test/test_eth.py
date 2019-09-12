from pytaraxa import eth

node_address = [
    "de2b1203d72d3549ee2f733b00b2789414c7cea5", "973ecb1c08c8eb5a7eaa0d3fd3aab7924f2838b0",
    "4fae949ac2b72960fbe857b56532e2d3c8418d5e", "415cf514eb6a5a8bd4d325d4874eae8cf26bcfe0",
    "b770f7a99d0b7ad9adf6520be77ca20ee99b0858"
]


def accounts():
    r = eth.accounts()
    print(r)


def getBalance():
    r = eth.getBalance(node_address[0])
    print(r)


def blockNumber():
    r = eth.blockNumber()
    print(r)


def getStorageAt():
    r = eth.getStorageAt()
    print(r)


def getTransactionCount():
    r = eth.getTransactionCount(address, 1)
    print(r)


def getBlockTransactionCountByHash():
    block = eth.getBlockByNumber('latest')
    hash = block['hash']

    r = eth.getBlockTransactionCountByHash(hash)
    print(r)


def getBlockByNumber():
    r = eth.getBlockByNumber('pending')
    print(r)


def getBlockByHash():
    block = eth.getBlockByNumber('latest')
    hash = block['hash']
    r = eth.getBlockByHash(hash)
    print(r)


def pendingTransactions():
    r = eth.pendingTransactions()
    print(r)


def sendTransaction():
    trx = {
        'from': 's',  #eth.accounts()[0],
        'to': node_address[2],
        'value': 10000,
        'gasPrice': 's',  #eth.gasPrice(),
        'gas': 100000,
        'nonce': 0
    }
    r = eth.sendTransaction(trx)
    return r


def get_all_balance():
    for add in node_address:
        print(eth.getBalance(add))


if __name__ == "__main__":
    #r = sendTransaction()
    #print(r)
    #print("=====number:%s" % eth.blockNumber())
    #get_all_balance()
    sendTransaction()
