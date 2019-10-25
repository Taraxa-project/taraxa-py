import json
import asyncio
import websockets
from . import NODE_WS_IP, NODE_WS_PORT, JSONRPC, ID


class Config():

    def __init__(self, ip=NODE_WS_IP, port=NODE_WS_PORT, jsonrpc=JSONRPC, id=ID):
        self.ip = ip
        self.port = port
        self.jsonrpc = jsonrpc
        self.id = id

    def __str__(self):
        return "ip:{},port:{},jsonrpc:{},id:{}".format(self.ip, self.port, self.jsonrpc, self.id)


config = Config()


def set_ws(params):
    if "ip" in params:
        config.ip = params["ip"]
    if "port" in params:
        config.port = params["port"]
    if "jsonrpc" in params:
        config.port = params["jsonrpc"]
    if "id" in params:
        config.port = params["id"]


def reset_ws():
    config.ip = NODE_WS_IP
    config.port = NODE_WS_PORT
    config.jsonrpc = JSONRPC
    config.id = ID


async def send_ws(data, callback, ip="", port=0):
    if not ip:
        ip = config.ip
    if not port:
        port = config.port

    while True:
        ws = await websockets.connect('ws://' + ip + ':' + str(port))
        await ws.send(data)
        try:
            async for msg in ws:
                _data = json.loads(msg)
                callback(_data)
        except Exception as e:
            print(e)
            print('\n<= 0 reconnect: %s\n' % data)
            await asyncio.sleep(0.1)


def message_ws(jsonrp, method, params, id):
    trx = {"jsonrpc": jsonrp, "method": method, "params": params, "id": id}
    return json.dumps(trx)


def traxa_rpc_ws(func):

    def wrap_func(*args, **kwargs):
        jsonrpc = kwargs.get("jsonrpc", config.jsonrpc)  #默认参数
        method = func.__name__  #jsonrpc方法名同函数名
        params, callback = func(*args, **kwargs)
        id = kwargs.get("id", config.id)  #默认参数
        ip = kwargs.get("ip", config.ip)
        port = kwargs.get("port", config.port)
        trx = message_ws(jsonrpc, method, params, id)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(send_ws(trx, callback, ip=ip, port=port))

    return wrap_func


@traxa_rpc_ws
def eth_subscribe(action, callback, **kwargs):
    params = [action]
    return params, callback


def newDagBlocks(callback, **kwargs):
    eth_subscribe("newDagBlocks", callback, **kwargs)


def newScheduleBlocks(callback, **kwargs):
    eth_subscribe("newScheduleBlocks", callback, **kwargs)


def newDagBlocksFinalized(callback, **kwargs):
    eth_subscribe("newDagBlocksFinalized", callback, **kwargs)


if __name__ == "__main__":
    callback = print
    newDagBlocksFinalized(callback)
