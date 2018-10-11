import asyncio
import aiohttp
from socket import *
from py00fib import fib


loop = asyncio.get_event_loop()


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


async def echo_handler(client):
    with client:
        while True:
            data = await loop.sock_recv(client, 10000)
            if not data:
                break
            await loop.sock_sendall(client, b'Got:' + bytes(fib(int(data))))
    print('Connection closed')


loop.create_task(echo_server(('', 25000)))
loop.run_forever()
