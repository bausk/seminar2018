from socket import *
import time

def benchmark(addr, nmessages):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(addr)
    while True:
        start = time.time()
        sock.send(b'28')
        resp = sock.recv(100)
        end = time.time()
        print((end-start), 'sec/message')

benchmark(('localhost', 25000), 100000)
