# Import socket module
import socket               
 
# Create a socket object
s = socket.socket()         
 
# Define the port on which you want to connect
port = 12345               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
# receive data from the server
message=s.recv(1024)
print(message.decode())

message='Hello i am client'
#
#message=List
byt=message.encode()
s.send(byt)
# close the connection
s.close()  