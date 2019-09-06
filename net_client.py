"""
File Name: net_client.py
Programmer: Daniel Ivan Lewis

Summary: This client program connects to the same port included in the net_server.py file.
It then receives and modifies a message that will then be sent back to the server. The program
continues until terminated.
"""

import socket

#Creating socket "sock" binding it to address "addr" and begining listening process
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 12021)
sock.connect(addr)

cont = True
while(cont):
    msg = input("Send a message: ")
    print(msg)
    sock.sendall(msg.encode())
    new_msg = sock.recv(1024).decode()
    print(new_msg)
    cont = input("Terminate program? Type 'y' for yes, 'n' for no")
    if cont == "y":
        cont = False
        sock.close()
        exit()
