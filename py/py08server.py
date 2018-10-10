import asyncio
from socket import *

loop = asyncio.get_event_loop()


def fib(n):
    if n < 2:
        return 0
    return fib(n - 1) + fib(n - 2)


async def echo_handler(client):
    with client:
        while True:
            data = await loop.sock_recv(client, 10000)
            if not data:
                break
            await loop.sock_sendall(client, b'Got:' + bytes(fib(int(data))))
    print('Connection closed')


async def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setblocking(0)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = await loop.sock_accept(sock)
        print('connection from', addr)
        asyncio.ensure_future(loop.create_task(echo_handler(client)))


loop.create_task(echo_server(('', 25000)))
loop.run_forever()
