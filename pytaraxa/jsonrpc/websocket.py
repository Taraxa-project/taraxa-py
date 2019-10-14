import json
import asyncio
import websockets

Node_ip = "0.0.0.0"
Node_port = 8777


async def ws_rpc(data, callback, ip=Node_ip, port=Node_port):
    while True:
        ws = await websockets.connect('ws://' + ip + ':' + str(port))
        await ws.send(data)
        try:
            async for message in ws:
                _data = json.loads(message)
                callback(_data)
        except:
            print('\n<= 0 reconnect: %s\n' % data)
            await asyncio.sleep(0.1)


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
        loop.run_until_complete(ws_rpc(trx, callback, ip=ip, port=port))

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
