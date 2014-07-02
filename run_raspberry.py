from socket import *
import sys
import time
from car import *


def run_raspberry():
	commands ={'forward':Car.forward,'back': Car.back, 'stop': Car.stop,'left': Car.left,'right': Car.right}
	HOST ='192.168.2.101'
	PORT = 8888
	s= socket(AF_INET, SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	print ('raspberry pi is listening on port 8888')
	while 1:
	    conn, addr = s.accept()
	
	    print ('Connected by:', addr)
	    while 1:
	            command= conn.recv(1024).replace('\n','')
	            if not command or command not in commands:break
	            commands[command]()
	    conn.close()
	    
if __name__ == '__main__':
	run_raspberry()

