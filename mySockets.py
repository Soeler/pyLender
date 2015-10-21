#coding: utf-8
##server.py
import sys
import socket     #import the socket library
import time

s = 1

class Client:
	def __init__(self, connection, address):
		global s
		self._connection = connection
		self._address = address
		data = self.receiveData()
		self.sendData("HTTP/1.1 200 OK\n\nteststring %d" % s)
		s += 1
		time.sleep(1)
	def __del__(self):
		print("closing connecton")
		self._connection.close()
	def sendData(self, data):
		self._connection.send(data.encode())
	def receiveData(self):
		data = self._connection.recv(4096)
		return data

class Server:	
	def __init__(self, HOST, PORT):
		self._HOST = HOST
		self._PORT = PORT
		#Create server socket
		self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#Prevent socket 'Time Waiting' state
		self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		#bind server socket to specified "IP" and port
		self._server.bind((HOST,PORT))
		print("server started")
		#maximum incoming connections
		self._server.listen(5)
		print("server: %s:%i" % (self._HOST, self._PORT))

	def __del__(self):
		print("closing Server")
		del self._HOST
		del self._PORT
		del self._server

	def acceptConnection(self):
		return self._server.accept()
