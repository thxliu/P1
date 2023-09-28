#!/usr/bin/env python3

import socket

# standard loopback interface address (localhost)
HOST = "127.0.0.1"  

# port to listen on (non-privileged ports are > 1023)
PORT = 65432  

# empty string msg to hold the decoded message
msg = ""

print("server starting - listening for connections at IP", HOST, "and port", PORT)

# creates a socket object and uses it without needing to call .close()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # associates the socket with a specific IP address and port number
    s.bind((HOST, PORT))

    # listening socket to allow the server to accept connections 
    s.listen(1)

    # accepts incoming connection request from client and returns a socket connected to the client
    conn, addr = s.accept()

    with conn:
        print(f"Connected established with {addr}")
        while True:

            #reads the data sent by the client and returns the length of the request in bytes
            data = conn.recv(1024)

            #decodes the data sent by the client
            msg = data.decode()

            #terminates loop if the data is an empty bytes object b''
            if not data:
                break
            print(f"Client equation has been received: '{data!r}' [{len(data)} bytes]")
            # print(f"echoing '{data!r}' back to client")

            total = 0
            equation_list = msg.split()
            num1 = int(equation_list[0])
            operation = equation_list[1]
            num2 = int(equation_list[2])

            if operation == "+":
                total = num1 + num2
            elif operation == "-":
                total = num1 - num2
            elif operation == "/":
                total = num1 / num2
            elif operation == "*":
                total = num1 * num2

            #converts the total from int to str 
            answer = str(total)

            #sends the encoded result to the client and sends data from bytes until all data has been sent
            conn.sendall(answer.encode())

print("server is done!")
