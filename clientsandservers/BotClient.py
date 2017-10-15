import sys
import socket

host = raw_input("please enter the public ip of the server:: ")

port = 5001

try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error, msg:
    print msg
    sys.exit()

while 1:
    clientSocket.sendto("client here!", (host, port))

    incoming = clientSocket.recvfrom(1024)
    incomingMsg = incoming[0]
    addr = incoming[1]

    print "server reply: ", incomingMsg
    toSend = raw_input("enter the message: ")

    if "Hasta La Vista" in toSend:
        clientSocket.sendto(toSend, (host, port))
        sys.exit()
    else:
        clientSocket.sendto(toSend, (host, port))