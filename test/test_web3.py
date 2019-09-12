from pytaraxa import web3


def clientVersion():
    r = web3.clientVersion()
    print(r)


def sha3():
    data = "0x68656c6c6f20776f726c64"
    r = web3.sha3(data)
    print(r)


if __name__ == "__main__":
    sha3()