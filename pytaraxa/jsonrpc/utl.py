def hex2int(s):
    if s == '':
        return -1
    n = int(s, 16)
    return n


def tag_check(tag):
    # tag data type:"latest",'10','0xa',10,0xa
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
