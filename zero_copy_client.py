# coding=utf-8
"""
desc..
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '16/5/6'
import os
import socket
import time


def zero_cp_send():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 4455)
    sock.connect(server_address)

    start = time.time()
    try:
        with open('/Users/fangpeng/Downloads/test.rar') as f:
            ret = 0
            offset = 0
            while True:
                # only python 3.x
                ret = os.sendfile(sock.fileno(), f.fileno(), offset, 65536)
                offset += ret
                if ret == 0:
                    break
    finally:
        sock.close()

    end = time.time()
    print('Total time: ', end-start)    # 2.803406000137329


zero_cp_send()