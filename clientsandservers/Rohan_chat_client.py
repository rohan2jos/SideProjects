import socket
import sys

# initialize the port number
port = 5001
host = 'localhost'
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error, msg:
    print msg
    sys.exit()

while 1:
    msg = raw_input("enter a message to send to the server:: ")
    s.sendto(msg, (host, port))

    d = s.recvfrom(1024)
    reply = d[0]
    addr = d[1]

    print "server reply: " + reply