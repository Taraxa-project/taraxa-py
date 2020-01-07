from path import workspace
from config import *
import web3


provider = web3.Web3.HTTPProvider("http://64.225.42.78:7777")
w3 = web3.Web3(provider=provider)

boot_address = w3.toChecksumAddress(boot_address)
address = w3.toChecksumAddress(address)
address_2 = w3.toChecksumAddress(address_2)


def get_info():
    r = w3.eth.blockNumber
    print(f"block number:{r}")

    r = w3.eth.getBalance(boot_address)
    print(f"boot address balance:{r}")

    r = w3.eth.getBalance(address)
    print(f"address balance:{r}")

    r = w3.eth.getBalance(address_2)
    print(f"address_2 balance:{r}")

    nonce = w3.eth.getTransactionCount(
        boot_address, block_identifier="pending")
    print(f"nonce:{nonce}")

    return nonce


def send_tx_boot():
    nonce = w3.eth.getTransactionCount(
        boot_address, block_identifier="pending")
    print(f"nonce:{nonce}")
    tx = w3.eth.account.signTransaction(
        {'nonce': nonce,
         'from': boot_address,
         'to': address,
         'value': 1000000000000000,
         'gas': GAS,
         'gasPrice': GASPRICE
         },
        boot_privateKey
    )
    r = w3.eth.sendRawTransaction(tx.rawTransaction)
    print(r)
    return r


def send_tx(_from, _to, private_key):
    nonce = w3.eth.getTransactionCount(
        _from, block_identifier="pending")
    tx = w3.eth.account.signTransaction(
        {'nonce': nonce,
         'from': _from,
         'to': _to,
         'value': 1000000000000000,
         'gas': GAS,
         'gasPrice': GASPRICE
         },
        private_key
    )
    r = w3.eth.sendRawTransaction(tx.rawTransaction)
    r = w3.toHex(r)
    return r


def get_tx(tx):
    r = w3.eth.getTransaction(tx)
    print(r)
    return r


def get_block_tx(block_number):
    r = w3.eth.getBlock(block_number)
    # print(r)
    tx = r['transactions'][0]
    return w3.toHex(tx)


def get_balance(address):
    r = w3.eth.getBalance(address)
    return r


def get_tx_by_block(block_number, id):
    r = w3.eth.getTransactionByBlock(block_number, id)
    print(r)
    return r


get_info()
#send_tx(address, address_2, privateKey)
