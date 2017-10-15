import socket
import select
import sys
from thread import *
import logging
import argparse

'''
basic config for logging
'''
logging.basicConfig(filename="logs/chat-server.log", level=logging.DEBUG, format='%(asctime)s %(funcName)5s() %(levelname)s:  %(message)s', datefmt='%I:%M:%S %p')

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    logging.error("cannot open socket")
    logging.error(msg)

'''
setting socket resuse, so that when the program is closed, the port is freed
'''
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    logging.error("wrong invocation of chat server, failing and exiting")
    print "correct usage: python chat_final.py <ipaddress> <port>"
    s.close()
    sys.exit()

'''
parsing the arguments:
- create an object of ArgumentParser()
- add host and port to tuple
- parse args as int
'''
p = argparse.ArgumentParser()
p.add_argument("host")
p.add_argument("port", type=int)
args = p.parse_args()

'''
catch args in variables and log
'''
host = args.host
port = args.port
logging.debug("ipaddress: " + str(host))
logging.debug("port: " + str(port))

try:
    s.bind((host, port))
except socket.error, msg:
    logging.error(msg)
    s.close()
    sys.exit()

s.listen(100)
clients = []

def client_thread(conn, addr):

    conn.send("server welcomes you to the chatroom")

    while True:
        try:
            incoming = conn.recv(2048)
            if incoming:
                logging.debug("received data:")
                logging.debug(incoming)
                print addr[0] + " -> " + incoming

                relay = addr[0] + " -> " + msg
                broadcast(relay, conn)
            else:
                logging.debug("looks like the socket is empty, meaning the connection is severed, closing")
                logging.debug("closing:")
                logging.debug(conn)
                remove(conn)
        except:
            continue

def broadcast(msg, conn):
    logging.debug("broadcasting: " + msg)
    for eachclient in clients:
        if eachclient != conn:
            try:
                logging.debug("sending message to client")
                logging.debug(eachclient)
                eachclient.send(msg)
            except:
                eachclient.close()
                logging.debug("looks like the conn is empty, meaning the connection is severed, closing")
                remove(conn)

def remove(conn):
    logging.debug("entered remove(), removing conn")
    if conn in clients:
        clients.remove(conn)

while True:
    conn, addr = s.accept()
    clients.append(conn)
    print addr[0] + " just connected!"
    start_new_thread(client_thread, (conn, addr))

logging.debug("closing socket")
s.close()