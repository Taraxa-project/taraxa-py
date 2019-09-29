from . import Node_ip, Node_port
from .utl import send, message, tag_check, traxa_rpc


@traxa_rpc
def net_version(**kwargs):
    params = []
    return params


@traxa_rpc
def net_peerCount(**kwargs):
    params = []
    return params


@traxa_rpc
def net_listening(**kwargs):
    params = []
    return params