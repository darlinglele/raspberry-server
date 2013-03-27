from socket import *
import threading
import sys
import time

HOST ='54.251.99.166'
PORT = 8888
def send(command):
	time.sleep(0.1)
	s= socket(AF_INET, SOCK_STREAM)
	s.connect((HOST, PORT))
	s.sendall('hello, world'+command)
	print 'data sent'+command
	data = s.recv(1024)
	print 'message from server:' + data
	s.close()
	
for x in range(0,100):
	t = threading.Thread(target = send,args=(str(x),))
	t.start()
	print 'new thread'

