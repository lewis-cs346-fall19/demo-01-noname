"""
File Name: net_server.py
Programmer: Daniel Ivan Lewis

Summary: This server program opens up a port and listens to it. When it accepts an incoming
connection it will keep running until the client program is terminated. The server receives an
incoming message and modifies it. The program will keep trying to search for a connection until
terminated.
"""

import socket

#Creating socket "sock" binding it to address "addr" and begining listening process
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 12021)
sock.bind(addr)
sock.listen(5)

while True:
    (connectedSock, clientAddress) = sock.accept()
    print("Accepted connection")
    try:
        msg = connectedSock.recv(1024).decode()
        print(msg)
        if not msg:
            break
        msg += " Received message is " + len(msg.split()) + " words long."
        print(msg)
        connectedSock.sendall(msg.encode())
    except:
        connectedSock.close()
