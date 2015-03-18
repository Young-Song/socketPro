#a server side implementation of a socket
from socket import *
serverPort = 12000
#Create a socket 
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('',serverPort))

print "The server is ready to receive"

while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	print message, clientAddress
	modifiedMessage = message.upper()
	serverSocket.sendto(modifiedMessage,clientAddress)
