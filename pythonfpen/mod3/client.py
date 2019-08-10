#!/usr/bin/python

import socket
import sys

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpSocket.connect((sys.argv[1], 8999))

while True:
	userInput = raw_input("Please enter message:")
	tcpSocket.send(userInput)
	print tcpSocket.recv(2048)

tcpSocket.close()
