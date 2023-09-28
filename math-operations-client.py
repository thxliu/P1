#!/usr/bin/env python3

import socket

 # the server's hostname or IP address
HOST = "127.0.0.1" 
# the port used by the server
PORT = 65432  

# asks client to input a number, operator, number to form the equation
MSG = input("Enter the operation in the form 'number operator number': ")

print("client starting - connecting to server at IP", HOST, "and port", PORT)

# creates a socket object and uses it without needing to call .close()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # connects to the server 
    s.connect((HOST, PORT))
    print(f"connection established, sending request '{MSG}'")

    # encodes the client's inputs and sends data from bytes to the server until all data has been sent
    s.sendall(MSG.encode())
    
    print("request sent, waiting for reply")

    # reads the server's reply
    data = s.recv(1024)
    

print(f"Received equation answer: '{data!r}' [{len(data)} bytes]")
print("client is done!")
