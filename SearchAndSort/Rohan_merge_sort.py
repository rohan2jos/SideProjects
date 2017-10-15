import random
import time

toSortArr = []
for m in range(0, 100000):
    nextNum = random.randint(0,20)
    toSortArr.append(nextNum)
anotherArr = toSortArr
#print "unsorted array " ,toSortArr

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        leftArr = arr[:mid]
        rightArr = arr[mid:]

        mergeSort(leftArr)
        mergeSort(rightArr)

        i = 0
        j = 0
        k = 0

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i = i + 1
            else:
                arr[k] = rightArr[j]
                j = j + 1
            k = k + 1

        while i < len(leftArr):
            arr[k] = leftArr[i]
            i = i + 1
            k = k + 1

        while j < len(rightArr):
            arr[k] = rightArr[j]
            j = j + 1
            k = k + 1

start = time.clock()
mergeSort(toSortArr)
end = time.clock()
totalMergeSortTime = end - start
print "[MergeSort] sorted in ", totalMergeSortTime
#print "ANSWER: " ,toSortArr


def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp

start_time = time.clock()
selectionSort(anotherArr)
end_time = time.clock()
totalSelectionSortTime = end_time - start_time
print "[SelectionSort] sorted in ",totalSelectionSortTime