from pytaraxa import taraxa
import pytaraxa.jsonrpc as rpc
node_address = [
    "de2b1203d72d3549ee2f733b00b2789414c7cea5", "973ecb1c08c8eb5a7eaa0d3fd3aab7924f2838b0",
    "4fae949ac2b72960fbe857b56532e2d3c8418d5e", "415cf514eb6a5a8bd4d325d4874eae8cf26bcfe0",
    "b770f7a99d0b7ad9adf6520be77ca20ee99b0858"
]


def dagBlockLevel():
    r = taraxa.dagBlockLevel()
    print(r)


def dagBlockPeriod():
    r = taraxa.dagBlockPeriod()
    print(r)


def getDagBlockByHash(hash):
    r = taraxa.getDagBlockByHash(hash)
    print(r)


def getDagBlockByLevel():
    r = taraxa.getDagBlockByLevel("latest")
    print(r)


def blockNumber():
    r = taraxa.blockNumber()
    print(r)


if __name__ == "__main__":
    blockNumber()