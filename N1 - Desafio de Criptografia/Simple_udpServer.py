from socket import *
from rsa import RSA

serverPort = 12500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("",serverPort))
print ("UDP server\n")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    text = str(message,"utf-8") #cp1252 #utf-8
    print('text '+str(text))

    rsa_crypt = RSA()

    d = int(input("\nChave privada d: "))

    n = int(input("\nChave privada n: "))

    msg = rsa_crypt.decrypt(int(text), d, n)

    print("\nReceived from Client: ", msg+"\n")