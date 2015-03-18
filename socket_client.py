#socket programming python
from socket import *

serverName = 'hostname'
serverPort = 12000

#Create a socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

#message
raw_input("Input lowercase sentence:")
clientSocket.sendto(message,(serverName,serverPort))


#modifiedMessage received from server  2048?
modifiedMessage,serverAddress  = clientSocket.recvfrom(2048)

print modifiedMessage

clientSocket.close()