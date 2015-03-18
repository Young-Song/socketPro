#socket programming python
from socket import *

#bind the receiving IP as localhost and receiving port number as 12000
serverName = '127.0.0.1'
serverPort = 12000

#Create a socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

#bind the sending port number as 12001
clientSocket.bind(('',12001))
#read message from keyboard and send it to server
while 1:
	message = raw_input("Input lowercase sentence:")
	clientSocket.sendto(message,(serverName,serverPort))


	#modifiedMessage received from server  2048?
	modifiedMessage,serverAddress  = clientSocket.recvfrom(2048)

	print modifiedMessage, serverAddress

#clientSocket.close()