from socket import *
import threading
import sys
import time

def execute(command):
	print command

def recv(conn):
	name = conn.recv(1024).replace('\n','')
	conn_list[name]=conn
	print name+ ' is connected'
	resp(conn,'Server: Hi'+ name)
    	while 1:
    	        command= conn.recv(1024).replace('\n','')
    	        execute(command)
    	        resp(conn, 'Hello Guy!')	   
    	conn.close()

def resp(conn,msg):
	try:
		conn.send(msg)
	except:
		print 'Error occured'
		import traceback
		traceback.print_exc()

HOST ='127.0.0.1'
HOST=gethostbyname(gethostname())
PORT = 8888
s= socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(100)
print ('listening on 8888')
conn_list ={}
while 1:
    conn, addr = s.accept()
    print ('Connected by:', addr)
    t=threading.Thread(target = recv, args=(conn,))
    t.start()

print ('Close the server...')
