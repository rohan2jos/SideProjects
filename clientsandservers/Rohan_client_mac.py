import socket
import pickle

arr = [3,4,1,6,5,9]

# swap function for the selection sort
def swap(min, j):
    temp = arr[min]
    arr[min] = arr[j]
    arr[j] = temp

# we are implementing the basic selection sort, will be changed to a better sort later
def sort():
    print "client has entered the sorting function"
    for i in range(len(arr)):
        min = i
        for j in range (i + 1, len(arr)):
            if arr[j] < arr[i]:
                min = j
    swap(min, j)


serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


SERVER_IP = "192.168.0.69"

PORT = 9998
i = 0
data = serversocket.recvfrom(1024)
print data
pickledArr = pickle.dumps(arr)
serversocket.sendto(pickledArr, (SERVER_IP, PORT))

serversocket.close()