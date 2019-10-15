from . import NODE_IP, NODE_PORT, JSONRPC, ID
import requests
import json


class Config():

    def __init__(self, ip=NODE_IP, port=NODE_PORT, jsonrpc=JSONRPC, id=ID):
        self.ip = ip
        self.port = port
        self.jsonrpc = jsonrpc
        self.id = id

    def __str__(self):
        return "ip:{},port:{},jsonrpc:{},id:{}".format(self.ip, self.port, self.jsonrpc, self.id)


config = Config()


def set(params):
    if "ip" in params:
        config.ip = params["ip"]
    if "port" in params:
        config.port = params["port"]
    if "jsonrpc" in params:
        config.port = params["jsonrpc"]
    if "id" in params:
        config.port = params["id"]


def reset():
    config.ip = NODE_IP
    config.port = NODE_PORT
    config.jsonrpc = JSONRPC
    config.id = ID


def send(data, ip="", port=0):
    if not ip:
        ip = config.ip
    if not port:
        port = config.port
    if type(data) == dict:
        data = json.dumps(data)
    elif type(data) == str:
        pass
    else:
        raise Exception('send data must be json string or dict')
    request = requests.post("http://{}:{}".format(ip, port), data=data)
    return request


def message(jsonrpc, method, params, id):
    trx = {"jsonrpc": jsonrpc, "method": method, "params": params, "id": id}
    return json.dumps(trx)


def traxa_rpc(func):

    def wrap_func(*args, **kwargs):
        #要提交的参数
        jsonrpc = kwargs.get("jsonrpc", config.jsonrpc)  #默认参数
        method = func.__name__  #jsonrpc方法名同函数名
        params = func(*args, **kwargs)
        id = kwargs.get("id", config.id)  #默认参数
        msg = message(jsonrpc, method, params, id)

        #要提交的节点
        ip = kwargs.get("ip", config.ip)
        port = kwargs.get("port", config.port)
        r = send(msg, ip, port)
        return r.json()

    return wrap_func