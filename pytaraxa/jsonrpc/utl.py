from . import Node_ip, Node_port
import requests
import json


def tag_check(tag):
    # "latest"
    # '10'
    # '0xa'
    # 10
    # 0xa
    if type(tag) == str:
        try:
            tag = hex(int(tag))
        except ValueError:
            try:
                tag = hex(int(tag, 16))  #16进制字符'0xa'
            except:
                tag = tag

    elif type(tag) == int:
        tag = hex(int(tag))

    return tag


def send(data, ip=Node_ip, port=Node_port):
    if type(data) == dict:
        data = json.dumps(data)
    elif type(data) == str:
        pass
    else:
        print('send data must be json string or dict')
        return None

    request = requests.post("http://{}:{}".format(ip, port), data=data)
    # except Exception as e:
    #     print(e)
    #     request = None
    return request


def message(jsonrpc, method, params, id):
    trx = {"jsonrpc": jsonrpc, "method": method, "params": params, "id": id}
    return json.dumps(trx)


def traxa_rpc(func):

    def wrap_func(*args, **kwargs):
        #要提交的参数
        jsonrpc = kwargs.get("jsonrpc", "2.0")  #默认参数
        method = func.__name__  #jsonrpc方法名同函数名
        params = func(*args, **kwargs)
        id = kwargs.get("id", 1)  #默认参数
        msg = message(jsonrpc, method, params, id)

        #要提交的节点
        ip = kwargs.get("ip", Node_ip)
        port = kwargs.get("port", Node_port)
        r = send(msg, ip, port)
        return r.json()

    return wrap_func