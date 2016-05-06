# coding=utf-8
"""
desc..
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '16/5/6'
import socket
import time


def normal_send():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 4455)
    sock.connect(server_address)
    start = time.time()

    try:
        with open('/Users/fangpeng/Downloads/test.rar') as f:       # 926MB
            data = f.read()
            sock.sendall(data)

    finally:
        sock.close()

    end = time.time()
    print('Total time: ', end-start)        # 6.221244812011719


normal_send()