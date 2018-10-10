
def send_request(data, address):
    print("Entered send, received data ", data)
    yield "HTTP 200 response"

def client_code():
    print("Entered client code")
    data = "foo"
    address = "localhost"
    result = yield data, address
    print("In coroutine: ", result)

def client_send():
    print("Entered client code")
    data = "foo"
    address = "localhost"
    result = yield from send_request(data, address)
    print("In coroutine: ", result)

