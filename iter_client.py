# coding=utf-8
"""
desc..
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.
"""
__date__ = '16/5/6'
import socket
import time


def readInChunks(fileObj, chunkSize=2048):
    """
    Lazy function to read a file piece by piece.
    Default chunk size: 2KB
    """
    while True:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data


def send_file(chunk_size):
    """
    Send big file client socket
    """
    start = time.time()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 4455)
    sock.connect(server_address)

    try:
        with open('/Users/fangpeng/Downloads/test.rar') as f:
            for chunk in readInChunks(f, chunkSize=chunk_size):
                sock.sendall(chunk)
    finally:
        sock.close()
    end = time.time()
    print('Total time: ', end-start)


if __name__ == '__main__':

    test_chunk_sizes = [
        1024*2,         # 2KB           # ('Total time: ', 6.821664810180664)
        1024*20,        # 2MB,          # ('Total time: ', 3.6460180282592773)
        1024*200,       # 20MB,         # ('Total time: ', 2.9026339054107666)
        1024*2000,      # 200MB,        # ('Total time: ', 2.0263049602508545)
        1024*3000,      # 300MB,        # ('Total time: ', 2.5401439666748047)
        1024*4000,      # 400MB,        # ('Total time: ', 2.111877202987671)
        1024*5000,      # 500MB,        # ('Total time: ', 2.186924934387207)
        1024*6000,      # 600MB,        # ('Total time: ', 2.3770549297332764)
        1024*7000,      # 600MB,        # ('Total time: ', 2.230679988861084)
        1024*8000,      # 600MB,        # ('Total time: ', 2.6439990997314453)
        1024*9000,      # 600MB,        # ('Total time: ', 2.1612918376922607)
        1024*10000,     # 1GB,          # ('Total time: ', 2.2416698932647705)
    ]
    for chunk_size in test_chunk_sizes:
        send_file(chunk_size)
        time.sleep(1)
