#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
MSG = input("Enter the operation in the form 'number operator number': ")

print("client starting - connecting to server at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"connection established, sending request '{MSG}'")
    s.sendall(MSG.encode())
    
    print("request sent, waiting for reply")
    data = s.recv(1024)
    

print(f"Received equation answer: '{data!r}' [{len(data)} bytes]")
print("client is done!")
