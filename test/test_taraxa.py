from pytaraxa import taraxa
from pytaraxa import eth
import pytaraxa.jsonrpc as rpc
node_address = [
    "de2b1203d72d3549ee2f733b00b2789414c7cea5", "973ecb1c08c8eb5a7eaa0d3fd3aab7924f2838b0",
    "4fae949ac2b72960fbe857b56532e2d3c8418d5e", "415cf514eb6a5a8bd4d325d4874eae8cf26bcfe0",
    "b770f7a99d0b7ad9adf6520be77ca20ee99b0858"
]


def dagBlockLevel():
    r = taraxa.dagBlockLevel(host='35.224.183.106')
    print(r)


def dagBlockPeriod():
    r = taraxa.dagBlockPeriod(host='34.66.1.140')
    print(r)


def getDagBlockByHash(hash, host):
    b = taraxa.getDagBlockByHash(hash)
    # print(b)
    print(' period: ', b['period'], ' level: ', b['level'], ' number: ', b['number'], ' hash: ',
          b['hash'])


def getDagBlockByLevel(level):
    r = taraxa.getDagBlockByLevel(level)
    if r:
        for b in r:
            print('dag   period: ', b['period'], ' level: ', b['level'], ' number: ', b['number'],
                  ' hash: ', b['hash'])
            _b = eth.getBlockByHash(b['hash'])
            if _b:
                print('block number: ', _b['number'], ' hash: ', _b['hash'])
            else:
                print('block no such block, hash:', b['hash'])
            print()


def blockNumber():
    r = taraxa.blockNumber()
    print(r)


if __name__ == "__main__":
    # dagBlockLevel()
    # dagBlockPeriod()
    #hash = '0x841a0296cf0afc3f5c281593af4528cf840744f6589760cdad9bed0fb3af477b'
    # getDagBlockByLevel(3)
    #hash = '0x326f8020ccd18e8ce783158926214a4ab1805b89855f80afb67a0dbe7bf385e3'
    hash = '0x478d82494a35aa2fb4eb6b6dd73b405eef37387c2873f4740a0fd3c14e811708'
    getDagBlockByHash(hash, host='127.0.0.1')
    # block = eth.getBlockByHash(
    #     '0xb0bdf5bf044fde7d5ec9633e82ff08a1e689aa63fea65af6ec655e91e1cb4d4b',
    #     fullTransactions=True)
    # print(block)
