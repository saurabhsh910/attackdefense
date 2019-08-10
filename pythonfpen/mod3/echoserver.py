#!/usr/bin/python

import socket

tcpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
tcpSocket.bind(("0.0.0.0", 8999))
tcpSocket.listen(2)

print "Waiting for a client"

(client, (ip,port)) = tcpSocket.accept()

client.send("Welcome to the SPSE course")

data = "dummy"

while len(data):

    data = client.recv(2048)
    print "Client sent: ", data
    client.send(data)

print "Client Closing"
client.close()

print "Socket closing"
tcpSocket.close()
