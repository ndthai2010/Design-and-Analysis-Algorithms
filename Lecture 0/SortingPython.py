def inputArray():
    array = []
    print("Number of elements:")
    n = input()
    array = n.split()
    for i in range(0, len(array)):
       array[i] = input()
    return array

def bubbleSort(array):
    r = array
    for i in range(0, len(r)):
        for j in range(i + 1, len(r)):
            if r[i] > r[j]:
                temp = r[i]
                r[i] = r[j]
                r[j] = temp
    return r

def shiftElement(array, i):
    r = array
    iValue = r[i]
    while (i > 0 & r[i - 1] > iValue):
        r[i] = r[i - 1]
        i = i - 1
    r[i] = iValue

def insertionSort(array):
    r = array
    for i in range(1, len(r)):
        if r[i] < r[i - 1]:
            shiftElement(r, i)
    return r


def selectionSort(array):
    r = array
    for i in range(0, len(r)):
        for j in range(i + 1, len(r)):
            min = r[i]
            if min > r[j]:
                temp = r[i]
                r[i] = r[j]
                r[j] = temp
    return r

def printArray(r):
    print(*r)

array = inputArray()
r = bubbleSort(array)
printArray(r)   

            
            
            
            
        
    
    
    

    