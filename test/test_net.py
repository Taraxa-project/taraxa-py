from pytaraxa import net


def version():
    r = net.version()
    print(r)


def peerCount():
    r = net.peerCount()
    print(r)


def listening():
    r = net.listening()
    print(r)


if __name__ == "__main__":
    listening()
