
import web3
import time

GAS = 7000000
GASPRICE = 10000000

boot_privateKey = "0x3800b2875669d9b2053c1aff9224ecfdc411423aac5b5a73d7a45ced1c3b9dcd"
boot_publicKey = "0x7b1fcf0ec1078320117b96e9e9ad9032c06d030cf4024a598347a4623a14a421d4f" \
    "030cf25ef368ab394a45e920e14b57a259a09c41767dd50d1da27b627412a"
boot_address = "0xde2b1203d72d3549ee2f733b00b2789414c7cea5"

privateKey = "0x5076e3eae916b0c68b72a514a67fd089c643c2f306462bb64a99155bfb26757d"
publicKey = "0x45df55840c79080d0f6fa445a6ec81a758e9b8df80083b1970c661e096000fce586ae389b58e1b9c6b5346bd912bccf656f84c1506b47681a63e0997c610c99b"
address = "0x07162012099a6c3d44b264cd70aa9f390a26a0f3"

privateKey_2 = '0x5f63bb17f902989d5a354f7048fd1bcd13e7e76e6b228918c0a61458d5c1206a'
address_2 = '0xa16A181AD474C82D8753eB0C10e8DD4e5710314f'


provider = web3.Web3.HTTPProvider("http://64.225.42.78:7777")
w3 = web3.Web3(provider=provider)

boot_address = w3.toChecksumAddress(boot_address)
address = w3.toChecksumAddress(address)
address_2 = w3.toChecksumAddress(address_2)

print(boot_address)


def get_info():
    r = w3.eth.blockNumber
    print(f"block number:{r}")

    r = w3.eth.getBalance(boot_address)
    print(f"boot address balance:{r}")

    r = w3.eth.getBalance(address)
    print(f"address      balance:{r}")

    r = w3.eth.getBalance(address_2)
    print(f"address_2    balance:{r}")


def send_tx_boot(address, nonce=None):
    if not nonce:
        nonce = w3.eth.getTransactionCount(
            boot_address, block_identifier="pending")
    print(f"nonce:{nonce}, address:{boot_address}")
    tx = w3.eth.account.signTransaction(
        {'nonce': nonce,
         'from': boot_address,
         'to': address,
         'value': 10000000000000,
         'gas': GAS,
         'gasPrice': GASPRICE
         },
        boot_privateKey
    )
    r = w3.eth.sendRawTransaction(tx.rawTransaction)
    r = w3.toHex(r)
    print(f'tx:{r}')
    return r


def send_tx(_from, _to, private_key, nonce=None):
    if not nonce:
        nonce = w3.eth.getTransactionCount(
            _from, block_identifier="pending")
    print(f"nonce:{nonce},address:{_from}")
    tx = w3.eth.account.signTransaction(
        {'nonce': nonce,
         'from': _from,
         'to': _to,
         'value': 1000000000000,
         'gas': GAS,
         'gasPrice': GASPRICE
         },
        private_key
    )
    r = w3.eth.sendRawTransaction(tx.rawTransaction)
    r = w3.toHex(r)
    print(f'tx:{r}')
    return r


def get_tx(tx):
    r = w3.eth.getTransaction(tx)
    print(r)
    return r


def get_block_tx(block_number):
    r = w3.eth.getBlock(block_number)
    tx = r['transactions'][0]
    return w3.toHex(tx)


def get_balance(address):
    r = w3.eth.getBalance(address)
    return r


def get_tx_by_block(block_number, id):
    r = w3.eth.getTransactionByBlock(block_number, id)
    print(r)
    return r


def run():
    i = 0
    while True:
        i += 1
        print(f"======== {i}")
        get_info()
        nonce = w3.eth.getTransactionCount(
            boot_address, block_identifier="pending")
        tx = send_tx_boot(address, nonce)
        r = w3.eth.waitForTransactionReceipt(tx)
        print("tx finished.")


if __name__ == "__main__":
    # pass
    # run()
    get_info()
