import socket, pickle

def swap(i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def sort():
    n = len(arr)
    for i in range(n):
        print " i is currently ", arr[i]

        for j in range(i + 1, len(arr)):
            print "-- j is currently ", arr[j]

            if arr[i] > arr[j]:
                print "arr[i] > arr[j], swapping", arr[i], arr[j]
                swap(i, j)



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 9999

host = socket.gethostname()

serversocket.connect((host, port))

tm = serversocket.recv(2048)

print "Received data from the server"
arr = pickle.loads(tm)
sort()
sorted = pickle.dumps(arr)
serversocket.send(sorted)
serversocket.close()
print "the client has sorted the array"
print "CLIENT: ", arr