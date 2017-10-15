arr = [9, 3, 5, 1, 6, 8, 7]
def swap(i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble():
    n = len(arr)
    for i in range(n):

        for j in range(i + 1, len(arr)):


            if arr[i] > arr[j]:
                swap(i, j)
    return arr

bubble()