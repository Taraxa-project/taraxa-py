from . import NODE_HOST, NODE_PORT, JSONRPC, ID
import requests
import json
import logging


class Config():

    def __init__(self, host=NODE_HOST, port=NODE_PORT, jsonrpc=JSONRPC, id=ID):
        self.host = host
        self.port = port
        self.jsonrpc = jsonrpc
        self.id = id

    def __str__(self):
        return "host:{},port:{},jsonrpc:{},id:{}".format(self.host, self.port, self.jsonrpc, self.id)


config = Config()


def set(params):
    if "host" in params:
        config.host = params["host"]
    if "port" in params:
        config.port = params["port"]
    if "jsonrpc" in params:
        config.port = params["jsonrpc"]
    if "id" in params:
        config.port = params["id"]


def reset():
    config.host = NODE_HOST
    config.port = NODE_PORT
    config.jsonrpc = JSONRPC
    config.id = ID


def send(data, *args, **kwargs):
    if type(data) == dict:
        data = json.dumps(data)
    elif type(data) == str:
        pass
    else:
        raise Exception('send data must be json string or dict')

    # print(kwargs)
    host = kwargs.get("host", config.host)
    port = kwargs.get("port", config.port)

    # print(host)
    # print(port)
    if (host.startswith('http') or host.startswith('https')) and not port:
        url = f"{host}"
    else:
        url = f"http://{host}:{port}"

    headers = {'Content-Type': 'application/json',
               'User-Agent': "Web3.py/5.2.2/<class 'web3.providers.rpc.HTTPProvider'>"}

    response = requests.post(url, data=data, headers=headers)

    return response


def message(jsonrpc, method, params, id):
    trx = {"jsonrpc": jsonrpc, "method": method, "params": params, "id": id}
    return json.dumps(trx)


def traxa_rpc(func):

    def wrap_func(*args, **kwargs):
        # 要提交的参数
        jsonrpc = kwargs.get("jsonrpc", config.jsonrpc)  # 默认参数
        method = func.__name__  # jsonrpc方法名同函数名
        params = func(*args, **kwargs)
        id = kwargs.get("id", config.id)  # 默认参数
        msg = message(jsonrpc, method, params, id)

        # print(kwargs)

        # 要提交的节点
        host = kwargs.get("host", config.host)
        port = kwargs.get("port", config.port)
        r = send(msg, host=host, port=port)
        return r.json()

    return wrap_func
