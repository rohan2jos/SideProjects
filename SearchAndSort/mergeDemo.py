import random

def mainFunct():
    arr = []
    '''
    for i in range(0, 20):
        nextNum = random.randint(0, 20)
        arr.append(nextNum)
    '''
    arr = [5,1,3,9,0,11,77,33,76]
    merge(arr)
    return arr

def merge(arr):


    '''
    1. find the breaking condition
    2. find the generalized equation
    '''

    if len(arr) > 1:
        '''
        array still holds more than 1 element, keep splitting
        '''

        mid = len(arr) // 2
        leftArr = arr[:mid]
        rightArr = arr[mid:]

        merge(leftArr)
        merge(rightArr)

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

        '''
        we hit this when one of the two is empty
        '''

        while i < len(leftArr):
            arr[k] = leftArr[i]
            i = i + 1
            k = k + 1

        while j < len(rightArr):
            arr[k] = rightArr[j]
            j = j + 1
            k = k + 1


mainFunct()