#!/usr/bin/python


import socket
import SocketServer



class EchoHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		print "Got connection from:", self.client_address
		data="dummy"
		
		while len(data):
			data = self.request.recv(2048)
			print "CLient send" + " " + data
			self.request.send(data)
		

serverAddr = ("0.0.0.0", 8999)
server = SocketServer.TCPServer(serverAddr, EchoHandler)
server.serve_forever()
