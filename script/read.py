def read_to_write_init():
    with open("pytaraxa/eth/methods.py") as f:
        lines = f.readlines()
    for l in lines:
        if l.startswith('def'):
            func_name = l.strip('def ').split('(')[0]
            print('from .methods import %s' % func_name)


def read_to_write_class():
    with open("pytaraxa/eth/methods.py") as f:
        lines = f.readlines()
    for l in lines:
        if l.startswith('def'):
            l1 = '    ' + l.replace('(', '(self,')
            l2 = l.replace('def ', '        eth.').replace(
                '**kwargs', 'ip=self.ip, port=self.port,**kwargs').replace(':', '')
            l3 = l.replace('def ', 'eth.').replace(', **kwargs', '').replace('**kwargs',
                                                                             '').replace(':', '')
            #print(l1)
            print(l3)


if __name__ == "__main__":
    read_to_write_class()