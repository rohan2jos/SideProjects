import socket
import sys
port = 5001

host = ""

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error, msg:
    print msg
    sys.exit()

try:
    s.bind((host, port))
except socket.error, msg:
    print msg
    sys.exit()

# try and receive a message from the connected socket
while 1:
    d = s.recvfrom(1024)
    print "client says: ", d
    data = d[0]
    addr = d[1]


    replyMsg = raw_input("enter a message to send to the client: ")
    if not data:
        break
    else:
        if replyMsg == 'exit':
            sys.exit()
    reply = replyMsg

    s.sendto(reply, addr)

s.close()