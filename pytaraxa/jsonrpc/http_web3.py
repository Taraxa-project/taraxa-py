from . import Node_ip, Node_port
from .utl import send, message, tag_check, traxa_rpc


# TODO
@traxa_rpc
def web3_clientVersion(**kwargs):
    params = []
    return params


# TODO
@traxa_rpc
def web3_sha3(data, **kwargs):
    params = [data]
    return params