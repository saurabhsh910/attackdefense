#!/usr/bin/python

import socket
from threading import Thread
from SocketServer import ThreadingMixIn

#Multithreaded python server: TCP server socket thread pool
class ClientThread(Thread):
	
	def __init__(self,ip,port):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		print "New server socket thread started"
	def run(self):
		while True : 
            		data = client.recv(2048) 
            		print "Server received data:", data
            		MESSAGE = raw_input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            		if MESSAGE == 'exit':
                		break
            		client.send(MESSAGE)

tcpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
tcpSocket.bind(("0.0.0.0", 8999))
#tcpSocket.listen(4)

print "Waiting for a client"

#(client, (ip,port)) = tcpSocket.accept()

#client.send("Welcome to the SPSE course")

data = "dummy"
threads = []

while True:
    tcpSocket.listen(4)
    print "Multithreaded server: Waiting for connections"
    (client, (ip,port)) = tcpSocket.accept()
    newthread = ClientThread(ip,port)
    newthread.start()
    threads.append(newthread)

for t in threads:
	t.join()
    #data = client.recv(2048)
    #print "Client sent: ", data
    #client.send(data)

print "Client Closing"
client.close()

print "Socket closing"
tcpSocket.close()
