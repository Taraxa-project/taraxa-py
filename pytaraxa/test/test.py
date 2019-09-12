from .. import eth


def blockNumber():
    r = eth.blockNumber()
    print(r)


if __name__ == "__main__":
    test()
