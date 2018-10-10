
async def send_request(data, address):
    print("Entered send, received data ", data)
    return "HTTP 200 response"


async def client_send():
    print("Entered client code")
    data = "foo"
    address = "localhost"
    result = await send_request(data, address)
    print("In coroutine: ", result)

