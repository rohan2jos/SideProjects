import socket
import os.path
import time
import json
import signal
import pymongo
'''

Development

D1: using biderectional socket
    - Completed on:

Changes:

I1: Conversion of blacklist into dictionary
    - Completed on: 03/23

I2: Connection of mongodb
    - Completed on:

I3: Insertion and retrieval from mongo
    - Completed on:
'''

dt = time.strftime("%Y-%m-%d %H:%M")

class Proxy:


    '''
    creating a blank object which will be associated with a file once a check is performed
    through the constructor
    '''
    file = object()

    def __init__(self):
        self.openFile()
        print "back to __init__"

        print dt + " [Proxy.__init__()] entered the Proxy class \n"

    def create_and_listen(self, add):

        PORT = 80

        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        serversocket.connect((add, PORT))
        '''
        serversocket.send(b"GET / HTTP/1.1\nHost: " + add +"\n\n")
        '''
        serversocket.send(b"GET / HTTP/1.1\nHost: " + add +"\r\nConnection: close\r\n\r\n")
        result = serversocket.recv(1024)
        serversocket.close()
        l3 = dt + " response:: \n" + result
        print result
        self.file.write(l3)

    '''
    open a file after performing a check if the log exists
    if the log exists, it will delete the old log and create a new one with the same name
    '''
    def openFile(self):
        if os.path.exists("proxylog"):
            print dt + " log exists, cleaning"
            os.remove("proxylog")
        self.file = open("proxylog", "w")
        l = dt + " starting log\n"
        self.file.write(l)

    '''
    performs a check on the blacklist comparing each entry to the user address
    if an entry in the blacklist matches the user address, it will abort, else, forward
    '''
    def visit(self, add):
        log = dt + " [Proxy.visit()] user is trying to visit: " + add + "\n"
        print log
        l = dt +  " [Proxy.visit()] checking blacklist \n"
        self.file.write(log)
        self.file.write(l)
        flag = 0

        with open("blacklist.json") as json_file:
            data = json.load(json_file)

            for p in data["addresses"]:
                if p["url"] in add:
                    l3 = dt + " [Proxy.visit()] address partially/fully matches: " + p["url"] + " ( in blacklist ) " + " in user attempt: " + add + "\n"
                    print l3
                    self.file.write(l3)
                    l1 = dt + " [Proxy.visit()] address matches a record in the blacklist, aborting" + "\n"
                    print l1
                    self.file.write(l1)
                    flag = 1
                    print "ADDRESS IN BLACKLIST. ABORTING REQUEST"
                    break
        if flag != 1:
            l2 = dt + " [Proxy.visit()] address not in blacklist, forwarding" + "\n"
            print l2
            self.file.write(l2)
            self.create_and_listen(add)

instance = Proxy()
instance.visit("www.google.com/images")
instance.visit("stackoverflow.com")
