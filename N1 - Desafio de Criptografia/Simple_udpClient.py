from socket import *
from rsa import RSA

serverName = "192.168.0.51" # IPv4 // ::1 IPv6
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET6
print("UDP Client\n")

while 1:
    message = input("\nInput message: ")

    if message == "exit":
        break
    else:
        rsa_crypt = RSA()
        n, e, d = rsa_crypt.main()

        print("n:", n)
        print("e:", e)
        print("d:", d)

        message = str(rsa_crypt.encrypt(message, e, n))        

    clientSocket.sendto(bytes(message,"utf-8"), (serverName, serverPort))

clientSocket.close()
