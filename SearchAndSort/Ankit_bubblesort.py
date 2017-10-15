
def bubbleSort(list):
    print("Before bubble sort :")
    print(list)

    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp

    return list

list = [6,5,7,5,1]
print(bubbleSort(list))