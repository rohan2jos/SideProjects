def swap(i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp



arr = [9,3,5,1,6,8,7]
n = len(arr)
for i in range(n):
    print " i is currently ", arr[i]

    for j in range(i + 1, len(arr)):
        print "-- j is currently ", arr[j]

        if arr[i] > arr[j]:
            print "arr[i] > arr[j], swapping", arr[i], arr[j]
            swap(i, j)

print arr