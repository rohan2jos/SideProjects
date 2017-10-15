import socket
import pickle


'''
very important to open the port in the iptables (atleast on the ubuntu):
sudo iptables -A INPUT -p tcp --dport 9998 -j ACCEPT
sudo iptables -A OUTPUT -p tcp --dport 9998 -j ACCEPT
'''



PORT = 9998
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostName = socket.gethostbyname('0.0.0.0')
serversocket.bind((hostName, PORT))

print "test server is listening for connections"

'''
broken: if the server sending the message is removed, the array is received
needs fix
'''

while True:
    serversocket.sendto("server saying hello!", ('192.168.0.2', PORT))
    (data, addr) = serversocket.recvfrom(1024)
    recd = pickle.loads(data)
    print recd

