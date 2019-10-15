NODE_IP = "0.0.0.0"
NODE_PORT = 7777
NODE_WS_IP = "0.0.0.0"
NODE_WS_PORT = 8777
JSONRPC = "2.0"
ID = 1

from .utl import tag_check

from .http_eth import *
from .http_taraxa import *
from .http_web3 import *
from .http_net import *

from ._http import send, message, traxa_rpc, set, reset
from ._websocket import send_ws, message_ws, traxa_rpc_ws, set_ws, reset_ws
from ._websocket import eth_subscribe, newDagBlocks, newScheduleBlocks, newDagBlocksFinalized
