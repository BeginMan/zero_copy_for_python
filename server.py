# coding=utf-8
"""
desc..
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
from __future__ import division
__date__ = '16/5/6'
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
address = ('0.0.0.0', 4455)
sock.bind(address)
sock.listen(1)

while True:
    conn, client_address = sock.accept()
    size, i = 0, 0
    try:
        while True:
            data = conn.recv(65536)
            i += 1
            if data:
                size += len(data)
            else:
                print("recv done")
                break
        print('I:', i)
        print('Total size: ', size/1024/1024, 'MB')
        print('*'*20)
    finally:
        conn.close()