import socket, pickle
import random
import time

'''
Steps in socket server
1. create the socket object - ip v4 and tcp
2. declare the port that you want the socket to communicate on
3. get the host of the socket with the inbuilt method - socket.gethostbyname()
4. Once we have the socket, the port and the hostname, we just have to bind the socket to listen on that host and that port
5. write logic, common methods are - socket.accept(), socket.send()
'''

# 1. Create the socket object with ipv4 and tcp
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. create the port that we want to bind the socket to
port = 9999

# 3. Get the hostname, and then bind the socket to the host and port
host = socket.gethostname()
serversocket.bind(('', port))

# 4. we wil listen to upto 5 requests
serversocket.listen(5)

# take the array as input, and then use that to be sorted
size = 100
arr = []
for i in range(0, size):
    nextNum = random.randint(0, 10)
    arr.append(nextNum)

a = pickle.dumps(arr)
while True:
    clientSocket, addr = serversocket.accept()

    print "We got a connection"
    print str(addr)
    clientSocket.send(a)
    received = clientSocket.recv(20480)
    recd = pickle.loads(received)
    print "client has returned the sorted arr"
    print recd
    clientSocket.close()