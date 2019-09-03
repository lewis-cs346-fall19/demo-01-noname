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
addr = ("0.0.0.0", 12021)
sock.bind(addr)
sock.listen(5)

while(1):
    (connectedSock, clientAddress) = sock.accept()
    try:
        msg = sock.recv(1024).decode()
        msg += " Received message is " + len(msg.split()) + " words long."
        print(msg)
        sock.sendall(msg.encode())
        break
    except ConnectionAbortedError:
        sock.close()





