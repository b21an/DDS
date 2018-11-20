#TEST CASE 1, python version 2.7.13

import socket                   # Import socket module
								                # this is for the main computer socket

port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()             # Create a socket object
host = ""
s.bind((host, port))            # Bind to the port
s.listen(1)                     # Now wait for client connection.

print 'Server listening....'

while True:
	conn, addr = s.accept()     		# Establish connection with client.
	print 'Got connection from', addr
	data = conn.recv(1024)        		# receive contents from client socket
	
	filename = "newfile.txt"      		# name is newfile txt for now, for testing purposes		
                                    #name will always correspond to time received in future test cases
	f = open(filename, "w+")			# copy contents to new file
	f.write(repr(data))
	f.close()
	
	conn.close()
