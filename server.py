from socket import *
import sys
import time
import detector

method ={'forward':detector.Car.forward,'back': detector.Car.back, 'stop':detector.Car.stop,'left':detector.Car.left,'right':detector.Car.right}
def execute(command):	
	print command
	method[command]()
HOST ='192.168.2.101'
PORT = 8888
s= socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print ('listening on 8888')
while 1:
    conn, addr = s.accept()

    print ('Connected by:', addr)
    while 1:
            command= conn.recv(1024).replace('\n','')
            if not command:break
            execute(command)
    conn.close()

print ('Close the server...')


