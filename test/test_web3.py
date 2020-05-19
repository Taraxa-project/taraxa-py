from path import workspace
from pytaraxa import web3

w3 = web3.Web3(host="64.225.42.78", port=7777)


def blockNumber():
    r = w3.eth.blockNumber()
    print(r)


def clientVersion():
    r = web3.clientVersion()
    print(r)


def sha3():
    data = "0x68656c6c6f20776f726c64"
    r = web3.sha3(data)
    print(r)


if __name__ == "__main__":
    blockNumber()
    # clientVersion()
