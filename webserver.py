#coding: utf-8

import server
import datetime
import threading

def defaultHttpResponse():
	response = "HTTP/1.1 200 OK\r\n"
	response += datetime.datetime.now().strftime("%A, %d %B %Y %H:%M:%S") + " GMT\r\n"
	response += "Server: Homebrew_by_Florian\r\n"
	response += "Connection: close\r\n"
	response += "Content-Type: text/html; charset=utf-8\r\n\r\n"
	return response

semaphore = threading.BoundedSemaphore(value=1)

myServer = server.Server("localhost", 8080)
while(1==1):
	#semaphore.acquire()
	(connection, address) = myServer.acceptConnection()
	t = threading.Thread(target = server.Client(connection, address))
	t.start()
	#semaphore.release()

del myServer
