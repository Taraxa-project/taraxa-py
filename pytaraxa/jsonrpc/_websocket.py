import json
import asyncio
import websockets

Node_ip = "0.0.0.0"
Node_port = 8777


async def ws_rpc(data, callback, node_ip=Node_ip, node_port=Node_port):
    ws = await websockets.connect('ws://' + node_ip + ':' + str(node_port))
    await ws.send(data)
    async for message in ws:
        data = json.loads(message)
        callback(data)


def json_trx(jsonrp, method, params, id):
    trx = {"jsonrpc": jsonrp, "method": method, "params": params, "id": id}
    return json.dumps(trx)


def traxa_rpc_ws(func):

    def wrap_func(*args, **kwargs):
        jsonrpc = kwargs.get("jsonrpc", "2.0")  #默认参数
        method = func.__name__  #jsonrpc方法名同函数名
        params, callback = func(*args, **kwargs)
        id = kwargs.get("id", 1)  #默认参数
        ip = kwargs.get("ip", Node_ip)
        port = kwargs.get("port", Node_port)
        trx = json_trx(jsonrpc, method, params, id)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(ws_rpc(trx, callback, node_ip=ip, node_port=port))

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
