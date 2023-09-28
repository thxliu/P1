#!/usr/bin/env python3

import socket


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
msg = ""

print("server starting - listening for connections at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print(f"Connected established with {addr}")
        while True:
            data = conn.recv(1024)
            msg = data.decode()
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

            answer = str(total)
            conn.sendall(answer.encode())
    conn.close()

print("server is done!")
