import socket
import sys
import os
import commands

host = ""
port = 5001

try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error, msg:
    print msg
    sys.exit()

# assuming the socket is created

try:
    serverSocket.bind((host, port))
except socket.error, msg:
    print msg
    sys.exit()

# assuming that the socket has been bound
# buffer size is set to 1024
while 1:
    incoming = serverSocket.recvfrom(1024)
    data = incoming[0]
    addr = incoming[1]

    if "ip" in data:
        print "The client is requesting for the ip"
        os.system('. ./GetPublicIp.sh')
        returnedPublicIp = os.environ["PUBLICIP"]
        serverSocket.sendto(str(returnedPublicIp), addr)

    if "Hasta La Vista" in data:
        print "kill command has been sent, ending server!"
        sys.exit()

    serverSocket.sendto("how may i help you", addr)


serverSocket.close()
