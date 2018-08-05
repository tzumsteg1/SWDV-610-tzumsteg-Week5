def bubbleSort(list):
    for values in range (0, len(list) - 1):
        for i in range (0, len(list) - 1 - values):
            #starts with first value and compares it with the second value. If the first value is larger, they swap positions.
            #then compares the next value the same way until in correct accending order
            if list[i] > listA[i + 1]:
                list[i], listA[i + 1] = list[i + 1], list[i]
    return list

def selectionSort(list):
    for i in range(len(list)):
        #searches through list to find the minimum value
        minVal = min(list[i:])
        #finds the position of the minimum value in terms of the list
        minIndex = list[i:].index(minVal)
        #replaces that minimum value at the index found
        list[i + minIndex] = list[i]
        #replace first element with min element
        list[i] = minVal  
    return list

def insertionSort(list):
    for i in range (1, len(list)):
        j = i - 1
        while list[j] > list[j + 1] and j >= 0:
            list[j], list[j + 1] = list[j + 1], list[j]
            j -= 1
    return list

#Chose to use three different lists to obtain the list 1 - 10
#This way I knew it actually sorted the list
listA = [1, 10, 9, 2, 3, 7, 8, 4, 5, 6]
listB = [1,9,10,8,3,5,7,6,2,4]
listC = [4, 2, 5, 6, 8, 9, 1, 10, 3, 7]

print(bubbleSort(listA))
print(selectionSort(listB))
print(insertionSort(listC))
