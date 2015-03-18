#A TCP client application
from socket import *
#define host name and port 
serverName = "localhost"
serverPort = 12000

# create a socket and bind its ip and port
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# read input from keyboard
sentence = raw_input("Input lowercase sentence:")

# send input to server 
clientSocket.send(sentence)

# read the capitalized sentence from the same socket 
modifiedSentence = clientSocket.recv(1024)

print "From Server:" , modifiedSentence

clientSocket.close();
