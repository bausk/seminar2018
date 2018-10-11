from time import sleep
from simplecoro import *

generator = client_code()
print("Generator: ", generator)
sleep(5)

user_input = generator.send(None)
print("Got: ", user_input)
sleep(5)

handler = send_request(*user_input)
print("Handler: ", handler)
sleep(5)

response = handler.send(None)
print("Response: ", response)
sleep(5)

generator.send(response)